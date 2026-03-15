import PostalMime from 'postal-mime'

interface Env {
  WEBHOOK_URL: string
  WEBHOOK_SECRET: string
}

async function computeHmac(message: string, secret: string): Promise<string> {
  const encoder = new TextEncoder()
  const key = await crypto.subtle.importKey(
    'raw',
    encoder.encode(secret),
    { name: 'HMAC', hash: 'SHA-256' },
    false,
    ['sign']
  )
  const signature = await crypto.subtle.sign('HMAC', key, encoder.encode(message))
  return Array.from(new Uint8Array(signature))
    .map(b => b.toString(16).padStart(2, '0'))
    .join('')
}

export default {
  async email(message: ForwardableEmailMessage, env: Env, ctx: ExecutionContext) {
    // Only process emails to newsletters@teahose.com
    if (message.to !== 'newsletters@teahose.com') {
      message.setReject('Unknown recipient')
      return
    }

    // Reject oversized emails (>5MB)
    if (message.rawSize > 5 * 1024 * 1024) {
      message.setReject('Email too large')
      return
    }

    try {
      // Parse the raw email
      const rawEmail = new Response(message.raw)
      const arrayBuffer = await rawEmail.arrayBuffer()
      const parser = new PostalMime()
      const email = await parser.parse(arrayBuffer)

      // Detect non-newsletter emails (confirmations, short emails, transactional)
      // and forward them to Gmail instead of processing
      const subject = (email.subject || '').toLowerCase()
      const textLen = (email.text || '').length
      const htmlLen = (email.html || '').length
      const contentLen = Math.max(textLen, htmlLen)

      const isConfirmation = /confirm|verify|activate|subscribe|opt.?in|double.?opt/i.test(subject)
        || (contentLen < 2000 && /confirm|verify|click here/i.test(email.text || email.html || ''))
      const isTooShort = contentLen < 500

      if (isConfirmation || isTooShort) {
        console.log(`Forwarding to Gmail (${isConfirmation ? 'confirmation' : 'too short'}): ${email.subject}`)
        await message.forward('altmbr@gmail.com')
        return
      }

      // Build payload
      const payload = JSON.stringify({
        from_address: email.from?.address || message.from,
        from_name: email.from?.name || '',
        subject: email.subject || '(no subject)',
        text: email.text || '',
        html: email.html || '',
        date: email.date || new Date().toISOString(),
        received_at: new Date().toISOString(),
      })

      // Compute HMAC signature
      const signature = await computeHmac(payload, env.WEBHOOK_SECRET)

      // POST to GCP Cloud Function
      const response = await fetch(env.WEBHOOK_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-Webhook-Signature': signature,
        },
        body: payload,
      })

      if (!response.ok) {
        const errorText = await response.text()
        console.error(`Webhook failed: ${response.status} ${errorText}`)
        // Forward to fallback on failure so content isn't lost
        await message.forward('altmbr@gmail.com')
      } else {
        console.log(`Processed: ${email.subject}`)
      }
    } catch (error) {
      console.error('Email processing error:', error)
      // Forward to fallback so content isn't lost
      await message.forward('altmbr@gmail.com')
    }
  },
}

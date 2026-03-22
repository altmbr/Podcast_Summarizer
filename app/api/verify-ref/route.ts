import { verifySubscriberRef } from '@/lib/tokens'
import type { NextRequest } from 'next/server'

export async function GET(request: NextRequest) {
  const ref = request.nextUrl.searchParams.get('ref')
  if (!ref) {
    return Response.json({ error: 'Missing ref parameter' }, { status: 400 })
  }

  const email = verifySubscriberRef(ref)
  if (!email) {
    return Response.json({ error: 'Invalid ref' }, { status: 403 })
  }

  return Response.json({ email })
}

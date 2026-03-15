import { NextRequest, NextResponse } from 'next/server'

interface Message {
  role: 'user' | 'assistant'
  content: string
}

interface ChatRequest {
  message: string
  transcript: string
  episodeTitle: string
  episodeSummary?: string
  conversationHistory: Message[]
}

export async function POST(request: NextRequest) {
  try {
    const body: ChatRequest = await request.json()
    const { message, transcript, episodeTitle, episodeSummary, conversationHistory } = body

    if (!process.env.ANTHROPIC_API_KEY) {
      return NextResponse.json(
        { error: 'Anthropic API key not configured' },
        { status: 500 }
      )
    }

    const systemPrompt = `You are a helpful AI assistant analyzing a podcast episode.

Episode Title: ${episodeTitle}

${episodeSummary ? `Episode Summary:\n${episodeSummary.substring(0, 1000)}\n\n` : ''}

Full Transcript (use this to answer questions):
${transcript.substring(0, 100000)}

Instructions:
- Answer questions based on the transcript content
- Provide specific quotes and timestamps when relevant
- Be concise but informative
- If something isn't covered in the transcript, say so
- Reference specific speakers when answering
- Format timestamps as [HH:MM:SS] when citing specific moments`

    const messages = [
      ...conversationHistory.slice(-10).map(msg => ({
        role: msg.role as 'user' | 'assistant',
        content: msg.content,
      })),
      { role: 'user' as const, content: message },
    ]

    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': process.env.ANTHROPIC_API_KEY,
        'anthropic-version': '2023-06-01',
      },
      body: JSON.stringify({
        model: 'claude-sonnet-4-6',
        max_tokens: 2048,
        system: systemPrompt,
        messages,
      }),
    })

    if (!response.ok) {
      const errorText = await response.text()
      console.error('Anthropic API error:', response.status, errorText)
      return NextResponse.json(
        { error: 'Failed to generate response' },
        { status: 500 }
      )
    }

    const data = await response.json()
    const text = data.content?.[0]?.text || 'No response generated.'

    return NextResponse.json({ response: text })
  } catch (error) {
    console.error('Chat API error:', error)
    return NextResponse.json(
      { error: 'Failed to generate response', details: error instanceof Error ? error.message : 'Unknown error' },
      { status: 500 }
    )
  }
}

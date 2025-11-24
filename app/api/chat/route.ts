import { GoogleGenerativeAI } from '@google/generative-ai'
import { NextRequest, NextResponse } from 'next/server'

const genAI = new GoogleGenerativeAI(process.env.GOOGLE_API_KEY || '')

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

    if (!process.env.GOOGLE_API_KEY) {
      return NextResponse.json(
        { error: 'Google API key not configured' },
        { status: 500 }
      )
    }

    // Use Gemini 2.0 Flash for fast, efficient responses
    const model = genAI.getGenerativeModel({ model: 'gemini-2.0-flash-exp' })

    // Build context-aware prompt
    const systemContext = `You are a helpful AI assistant analyzing a podcast episode.

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

    // Build conversation history for context
    const conversationContext = conversationHistory
      .slice(-10) // Last 10 messages for context
      .map(msg => `${msg.role === 'user' ? 'User' : 'Assistant'}: ${msg.content}`)
      .join('\n\n')

    const fullPrompt = `${systemContext}

Previous Conversation:
${conversationContext}

User Question: ${message}

Please provide a helpful, accurate answer based on the transcript.`

    // Generate response
    const result = await model.generateContent(fullPrompt)
    const response = result.response
    const text = response.text()

    return NextResponse.json({ response: text })
  } catch (error) {
    console.error('Chat API error:', error)
    return NextResponse.json(
      { error: 'Failed to generate response', details: error instanceof Error ? error.message : 'Unknown error' },
      { status: 500 }
    )
  }
}

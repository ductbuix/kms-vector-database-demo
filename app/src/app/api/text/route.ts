import { TextSearch } from '@/types/TextSearch'
import { NextRequest, NextResponse } from 'next/server'

const API_URL = process.env.API_URL

export async function GET(
  request: NextRequest,
): Promise<NextResponse<{ result: TextSearch[] }>> {
  const query = request.nextUrl.searchParams
  const text = query.get('text')

  const response = await fetch(`${API_URL}/text?text=${text}`).catch((e) => {
    console.error(e)
    return null
  })
  const data = await response?.json()

  return NextResponse.json(data)
}

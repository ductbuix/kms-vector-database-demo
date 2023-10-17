import { TextSearch } from '@/types/common'
import { API_URL } from '@/utils/env'
import { NextRequest, NextResponse } from 'next/server'

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

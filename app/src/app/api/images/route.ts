import { ImageSearch } from '@/types/common'
import { API_URL } from '@/utils/env'
import { NextRequest, NextResponse } from 'next/server'

export async function POST(
  request: NextRequest,
): Promise<NextResponse<ImageSearch>> {
  const formData = await request.formData()
  const response = await fetch(`${API_URL}/images`, {
    body: formData,
    method: 'POST',
  }).catch((e) => {
    console.error(e)
    return null
  })
  const data = await response?.json()

  return NextResponse.json(data)
}

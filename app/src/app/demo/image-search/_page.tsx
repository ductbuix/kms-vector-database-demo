'use client'

import { useCallback, useState } from 'react'
import SearchForm from './components/SearchForm'
import SearchResult from './components/SearchResult'
import { ImageSearch } from '@/types/common'
import { NEXT_PUBLIC_API_URL } from '@/utils/env'

type ImageSearchResponse = ImageSearch & { message: string }

export default function ImageSearchPage() {
  const [result, setResult] = useState<string[]>([])
  const [message, setMessage] = useState<string>()

  const handleSubmit = useCallback(async (file: File) => {
    const formData = new FormData()
    formData.append('file', file, file.name)

    await fetch(`/api/images`, {
      method: 'POST',
      body: formData,
    })
      .then((res): Promise<ImageSearchResponse> => res.json())
      .then((data: ImageSearchResponse) => {
        if (data?.result) {
          const { result } = data
          const mappedHostResult = result.map(
            (path) => `${NEXT_PUBLIC_API_URL}/images${path}`,
          )
          setResult(mappedHostResult)
        }
        setMessage(data?.message)
      })
  }, [])

  return (
    <>
      <SearchForm onSubmit={handleSubmit} />
      {message && <p className="mt-1 text-xs italic text-red-500">{message}</p>}

      <div className="mt-8">
        <SearchResult result={result} />
      </div>
    </>
  )
}

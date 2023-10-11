'use client'

import { useState } from 'react'
import { TextSearch } from '@/types/TextSearch'
import SearchForm from './components/SearchForm'
import SearchResult from './components/SearchResult'

export default function SemanticSearchPage() {
  const [results, setResults] = useState<TextSearch[]>([])
  const [message, setMessage] = useState<string>()

  const handleSubmit = async (text: string) => {
    await fetch(`/api/text?text=${text}`)
      .then((res) => {
        return res.json()
      })
      .then((data: { result: TextSearch[]; message?: string }) => {
        setResults(data?.result)
        setMessage(data?.message)
      })
  }

  return (
    <>
      <SearchForm onSubmit={handleSubmit} />
      {message && <p className="mt-1 text-xs italic text-red-500">{message}</p>}

      <div className="mt-4">
        <SearchResult results={results} />
      </div>
    </>
  )
}

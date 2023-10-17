'use client'

import { NEXT_PUBLIC_API_URL } from '@/utils/env'
import Image from 'next/image'
import React, { useCallback, useState } from 'react'

interface SearchFormProps {
  onSubmit: (file: File) => void
}

export default function SearchForm({ onSubmit }: SearchFormProps) {
  const [file, setFile] = useState<File>()

  const handleSubmit = useCallback(() => {
    if (file) {
      onSubmit(file)
    }
  }, [file])

  const handleChange = useCallback(
    (event: React.ChangeEvent<HTMLInputElement>) => {
      if (event.currentTarget.files) {
        setFile(event.currentTarget.files?.[0])
      }
      event.preventDefault()
    },
    [],
  )

  return (
    <form className="mt-4 inline-flex w-full">
      <input
        id="file"
        type="file"
        onChange={handleChange}
        accept="image/jpg,image/png"
        className="grow text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-violet-50 file:text-violet-700 hover:file:bg-violet-100"
      />
      <button
        type="button"
        className="sm:grow-0 grow text-white px-4 py-2 border border-zinc-100/20 bg-zinc-100/10 hover:bg-zinc-100/30 active:bg-zinc-100/20 disabled:text-gray-300 disabled:cursor-not-allowed transition-all"
        onClick={handleSubmit}
        disabled={!file}
      >
        Search
      </button>
    </form>
  )
}

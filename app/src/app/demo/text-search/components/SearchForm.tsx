'use client'

import { useCallback, useState } from 'react'

interface SearchFormProps {
  onSubmit: (text: string) => void
}

export default function SearchForm({ onSubmit }: SearchFormProps) {
  const [text, setText] = useState('')

  const handleSubmit = useCallback(() => {
    onSubmit(text)
  }, [text])

  const handleChange = useCallback((event: React.ChangeEvent<HTMLInputElement>) => {
    setText(event.currentTarget.value)
  }, [])

  const handleKeyDown = useCallback(
    (event: React.KeyboardEvent<HTMLInputElement>) => {
      if (event.key === 'Enter') {
        event.preventDefault()
        handleSubmit()
      }
    },
    [text],
  )

  return (
    <form className="mt-4 inline-flex w-full flex-wrap">
      <input
        className="grow h-8 px-2 py-5 border border-zinc-100/20 bg-zinc-100/10 active:bg-zinc-100/20 transition-all"
        id="search"
        name="search"
        type="text"
        placeholder="Search..."
        autoFocus
        value={text}
        onChange={handleChange}
        onKeyDown={handleKeyDown}
      />
      <button
        type="button"
        className="sm:grow-0 grow text-white px-4 py-2 border border-zinc-100/20 bg-zinc-100/10 hover:bg-zinc-100/30 active:bg-zinc-100/20 disabled:text-gray-300 disabled:cursor-not-allowed transition-all"
        onClick={handleSubmit}
        disabled={!text}
      >
        Search
      </button>
    </form>
  )
}

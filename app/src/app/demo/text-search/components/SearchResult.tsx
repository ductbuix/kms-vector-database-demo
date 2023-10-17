import { TextSearch } from '@/types/common'

interface SearchResultProps {
  results: TextSearch[]
}

export default function SearchResult({ results }: SearchResultProps) {
  return (
    <ul className="p-2 text-gray-200 flex flex-col gap-y-2 border border-zinc-100/20 max-w-full">
      {results?.map((result) => (
        <li key={result.id} className="break-words hover:bg-gray-100/30 transition-colors">{result.title}</li>
      ))}

      {!results?.length && (
        <li>
          <i>No results</i>
        </li>
      )}
    </ul>
  )
}

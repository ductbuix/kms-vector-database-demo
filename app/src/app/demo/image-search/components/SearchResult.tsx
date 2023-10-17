import { ImageSearch } from '@/types/common'
import Image from 'next/image'

type SearchResultProps = ImageSearch

export default function SearchResult({ result }: SearchResultProps) {
  return (
    <div className="grid grid-cols-3 auto-rows-auto gap-1">
      {result?.map((path) => {
        return (
          <Image
            src={path}
            alt={path}
            width={384}
            height={384}
            key={path}
            className="object-contain w-full h-auto"
          />
        )
      })}
      {result?.length === 0 && (
        <div className="flex justify-center items-center w-full h-full">
          <i>No results</i>
        </div>
      )}
    </div>
  )
}

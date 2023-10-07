import Link from 'next/link'

const routes = [
  {
    name: 'Home',
    href: '/',
  },
  {
    name: 'Semantic Search',
    href: '/demo/semantic-search',
  },
  {
    name: 'Image Search',
    href: '/demo/image-search',
  },
  {
    name: 'Similarity Image Search',
    href: '/demo/similarity-image-search',
  },
]

export default function Navigation() {
  return (
    <nav className="flex flex-col">
      {routes.map(({ name, href }) => (
        <Link
          key={href}
          className="text-xl text-left px-6 py-4 border-b border-zinc-100/30 hover:border-zinc-100/60 transition-all"
          href={href}
        >
          {name}
        </Link>
      ))}
    </nav>
  )
}

import Link from 'next/link'

const routes = [
  {
    name: 'Home',
    href: '/',
  },
  {
    name: 'Text Search',
    href: '/demo/text-search',
  },
  {
    name: 'Image Search',
    href: '/demo/image-search',
  },
  {
    name: 'Document Search',
    href: '/demo/document-search',
  },
]

export default function Navigation() {
  return (
    <nav className="flex flex-col">
      {routes.map(({ name, href }) => (
        <Link
          key={href}
          className="text-xl text-left px-6 py-4 border-b border-zinc-600 hover:border-zinc-900 dark:border-zinc-100/30 dark:hover:border-zinc-100/60 transition-all"
          href={href}
        >
          {name}
        </Link>
      ))}
    </nav>
  )
}

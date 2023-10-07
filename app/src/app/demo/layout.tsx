interface DemoLayoutProps {
  children: React.ReactNode
}

export default function DemoLayout({ children }: DemoLayoutProps) {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between py-24">
      <section className="w-2/3">{children}</section>
    </main>
  )
}

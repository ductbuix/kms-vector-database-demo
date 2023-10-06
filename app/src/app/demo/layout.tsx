interface DemoLayoutProps {
  children: React.ReactNode
}

export default function DemoLayout({ children }: DemoLayoutProps) {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between pt-24">
      {children}
    </main>
  )
}

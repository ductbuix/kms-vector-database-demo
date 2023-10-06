export default function Loading() {
  return (
    <>
      <div className="w-screen h-screen flex items-center justify-center bg-transparent">
        <span className="bg-transparent animate-spin rounded-full h-6 w-6 border-t-2 border-b-2 border-gray-900 dark:border-gray-200" />
      </div>
    </>
  )
}

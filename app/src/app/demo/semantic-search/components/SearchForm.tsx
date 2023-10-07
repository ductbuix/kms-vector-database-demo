export default function SearchForm() {
  return (
    <form className="mt-4">
      <input
        className="h-8 px-2 py-5 border border-zinc-100/20 bg-zinc-100/10 active:bg-zinc-100/20 transition-all"
        id="search"
        name="search"
        type="text"
        placeholder="Search..."
      />
      <button
        type="button"
        className="text-white px-4 py-2 border border-zinc-100/20 bg-zinc-100/10 hover:bg-zinc-100/30 active:bg-zinc-100/20 transition-all"
      >
        Search
      </button>
    </form>
  )
}

import SearchForm from './components/SearchForm'
import SearchResult from './components/SearchResult'

export default function SemanticSearchPage() {
  return (
    <div>
      <SearchForm />

      <div className="mt-4">
        <SearchResult />
      </div>
    </div>
  )
}

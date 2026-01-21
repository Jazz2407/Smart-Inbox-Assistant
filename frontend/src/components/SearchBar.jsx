function SearchBar({ setSearch }) {
  return (
    <div className="search-bar">
      <input
        type="text"
        placeholder="Search by subject..."
        onChange={e => setSearch(e.target.value)}
      />
    </div>
  );
}

export default SearchBar;

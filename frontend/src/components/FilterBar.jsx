function FilterBar({ setCategory }) {
  return (
    <div className="filter-bar">
      <label>Filter by Category: </label>
      <select onChange={e => setCategory(e.target.value)}>
        <option value="All">All</option>
        <option value="Important">Important</option>
        <option value="Promotion">Promotion</option>
        <option value="Spam">Spam</option>
      </select>
    </div>
  );
}

export default FilterBar;

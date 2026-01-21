import { useEffect, useState } from "react";
import { fetchEmails } from "../services/api";
import EmailCard from "../components/EmailCard";
import FilterBar from "../components/FilterBar";
import SearchBar from "../components/SearchBar";

function Inbox() {
  const [emails, setEmails] = useState([]);
  const [category, setCategory] = useState("All");
  const [search, setSearch] = useState("");

  useEffect(() => {
    fetchEmails().then(data => {
      let allEmails = [];
      Object.values(data.grouped_by_category).forEach(arr => {
        allEmails = [...allEmails, ...arr];
      });
      setEmails(allEmails);
    });
  }, []);

  const filteredEmails = emails.filter(email => {
    return (
      (category === "All" || email.category === category) &&
      email.subject.toLowerCase().includes(search.toLowerCase())
    );
  });

  return (
    <div className="container">
      <SearchBar setSearch={setSearch} />
      <FilterBar setCategory={setCategory} />
      {filteredEmails.map((email, index) => (
        <EmailCard key={index} email={email} />
      ))}
    </div>
  );
}

export default Inbox;

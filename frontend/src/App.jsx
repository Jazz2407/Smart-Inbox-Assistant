import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [emails, setEmails] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // 1. Fetch data from your backend when the app loads
  useEffect(() => {
    fetch('http://127.0.0.1:8000/gmail-emails')
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch emails');
        }
        return response.json();
      })
      .then(data => {
        setEmails(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Error fetching data:", err);
        setError("Could not connect to backend. Is it running?");
        setLoading(false);
      });
  }, []);

  // 2. Helper to get colors based on Priority
  const getPriorityColor = (priority) => {
    switch (priority?.toLowerCase()) {
      case 'high': return 'badge-high';
      case 'medium': return 'badge-medium';
      case 'low': return 'badge-low';
      default: return 'badge-default';
    }
  };

  if (loading) return <div className="loading">🤖 AI is reading your emails...</div>;
  if (error) return <div className="error">❌ {error}</div>;

  return (
    <div className="container">
      <header>
        <h1>📨 Smart Inbox Assistant</h1>
        <p>AI-Powered Organization</p>
      </header>

      <div className="email-list">
        {emails.map((email) => (
          <div key={email.id} className="email-card">
            <div className="card-header">
              <span className={`badge ${getPriorityColor(email.priority)}`}>
                {email.priority || 'Unknown'} Priority
              </span>
              <span className="badge badge-label">
                {email.label || 'Uncategorized'}
              </span>
              <span className="date">{email.date}</span>
            </div>

            <h2>{email.subject}</h2>
            <p className="sender">From: <strong>{email.from}</strong></p>
            <p className="snippet">{email.snippet}...</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
import "./EmailCard.css";

export default function EmailCard({ email }) {
  const priorityClass = email.priority.toLowerCase();

  return (
    <div className={`email-card ${priorityClass}`}>
      <div className="email-header">
        <span className={`priority badge ${priorityClass}`}>
          {email.priority.toUpperCase()} PRIORITY
        </span>

        <span className="label badge">
          {email.label.toUpperCase()}
        </span>

        <span className="email-date">{email.date}</span>
      </div>

      <h3 className="email-subject">{email.subject}</h3>

      <p className="email-from">From: {email.from}</p>

      <p className="email-snippet">{email.snippet}</p>
    </div>
  );
}

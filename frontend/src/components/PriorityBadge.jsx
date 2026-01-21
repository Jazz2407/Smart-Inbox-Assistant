function PriorityBadge({ score }) {
  let level = "low";

  if (score >= 10) level = "high";
  else if (score >= 6) level = "medium";

  return (
    <span className={`badge ${level}`}>
      Priority: {score}
    </span>
  );
}

export default PriorityBadge;

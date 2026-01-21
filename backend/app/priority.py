def calculate_priority(email):
    score = 0
    reasons = []

    sender = email["from"].lower()
    subject = email["subject"].lower()
    body = email["body"].lower()
    category = email["category"]

    if "boss" in sender or "manager" in sender:
        score += 5
        reasons.append("Sender is manager/boss")

    if any(word in subject + body for word in ["urgent", "deadline", "tomorrow"]):
        score += 4
        reasons.append("Time-sensitive content")

    if category == "Important":
        score += 3
        reasons.append("Marked as Important")

    if category == "Promotion":
        score += 1
        reasons.append("Promotional content")

    return {
        "score": score,
        "reason": ", ".join(reasons) if reasons else "Low priority"
    }

def generate_summary(body: str) -> str:
    sentences = body.split(".")
    return sentences[0].strip() + "."


def generate_reply(category: str, subject: str) -> str:
    if category == "Important":
        return f"Thank you for the update regarding '{subject}'. I will take action shortly."
    elif category == "Promotion":
        return "Thank you for sharing this information. I will review it if needed."
    elif category == "Spam":
        return "This message looks suspicious. No reply will be sent."
    else:
        return "Thank you for reaching out."


def suggest_action(category: str) -> str:
    if category == "Important":
        return "reply"
    elif category == "Promotion":
        return "optional_reply"
    elif category == "Spam":
        return "ignore"
    else:
        return "review"

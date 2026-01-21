


from app.gmail_service import fetch_gmail_emails

def process_emails():
    emails = fetch_gmail_emails()
    return emails


    for email in emails:
        ai_result = analyze_email(email["subject"], email["body"])

        email_data = {
            "from": email["from"],
            "subject": email["subject"],
            "snippet": email["snippet"],
            "date": email["date"],
            "priority": ai_result["priority"],
            "label": ai_result["label"]
        }

        

        results.append(email_data)

    return results

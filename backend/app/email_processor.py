import time
from app.gmail_service import fetch_unread_messages
from app.ai_classifier import analyze_email_with_llm
from app.database import db

async def process_new_emails():
    # EXTREME SAFETY MODE: Fetch only 1 email
    print("Fetching 1 email to test API health...")
    raw_emails = fetch_unread_messages(limit=1)
    
    if not raw_emails:
        print("No unread emails found.")
        return []

    processed_results = []
    email = raw_emails[0] # Take the first one

    print(f"Attempting to process: {email['subject']}")
    
    # Try 3 times with LONG delays
    ai_result = None
    for attempt in range(3):
        ai_result = analyze_email_with_llm(
            sender=email['sender'], 
            subject=email['subject'], 
            body=email['snippet']
        )
        
        # If we hit the quota, wait 60 seconds (Yes, a full minute)
        if "429" in ai_result.summary:
            print(f"⚠️ Quota hit on attempt {attempt+1}. Waiting 60 seconds...")
            time.sleep(60) 
            continue 
        else:
            # Success!
            print("✅ Success! API is working.")
            break
    
    # Save result
    full_record = {
        **email,
        "analysis": ai_result.model_dump()
    }
    db.save_email(full_record) 
    processed_results.append(full_record)

    return processed_results
from fastapi import FastAPI
from app.email_processor import process_new_emails
from app.database import db # Import the database we fixed

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Smart Inbox API is running!"}

# 1. TRIGGER: This tells the AI to go fetch and analyze emails
@app.post("/api/refresh-inbox")
async def refresh_inbox():
    results = await process_new_emails()
    return {"status": "success", "new_emails": results}

# 2. READ: This is what your Frontend will eventually fetch
@app.get("/api/emails")
def get_emails():
    return db.get_all_emails()
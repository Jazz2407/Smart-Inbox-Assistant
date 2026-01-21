import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from app.model import SmartEmailAnalysis

load_dotenv()

def analyze_email_with_llm(sender: str, subject: str, body: str) -> SmartEmailAnalysis:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return SmartEmailAnalysis(
            category="Work", priority="Low", summary="Missing API Key", suggested_action="None"
        )

    genai.configure(api_key=api_key)
    
    # ---------------------------------------------------------
    # FIX: Use 'gemini-2.5-flash' (The 2026 Standard)
    # ---------------------------------------------------------
    model = genai.GenerativeModel(
        'gemini-2.5-flash', 
        generation_config={"response_mime_type": "application/json"}
    )

    prompt = f"""
    You are a smart inbox assistant. Analyze this email.
    
    Email Details:
    - From: {sender}
    - Subject: {subject}
    - Body: {body[:1000]}

    Instructions:
    1. Output valid JSON only.
    2. Category options: "Work", "Personal", "Newsletter", "Security", "Spam".
    3. Priority options: "High", "Medium", "Low".
    4. Suggested Action options: "Reply", "Archive", "Create Task", "None".

    JSON Schema:
    {{
        "category": "String",
        "priority": "String",
        "summary": "String",
        "suggested_action": "String",
        "action_detail": "String or null"
    }}
    """

    try:
        response = model.generate_content(prompt)
        # Gemini 2.5 is very good at native JSON, but we keep the cleanup just in case
        clean_text = response.text.replace("```json", "").replace("```", "").strip()
        data = json.loads(clean_text)
        return SmartEmailAnalysis(**data)

    except Exception as e:
        print(f"Gemini AI Error: {e}")
        return SmartEmailAnalysis(
            category="Work", priority="Low", summary=f"Error: {str(e)[:50]}", suggested_action="None"
        )
from google import genai
import os
from dotenv import load_dotenv

# Load your .env file so it finds the API key
load_dotenv()

# explicit api_key if needed, otherwise it uses os.environ["GOOGLE_API_KEY"]
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY")) 

print("Fetching available models for your API key...")
try:
    for model in client.models.list():
        # Only show models that support generating content
        if "generateContent" in model.supported_actions:
            print(f"✅ Available: {model.name}")
            # The 'name' usually looks like "models/gemini-1.5-flash"
            # You just use the part after "models/"
except Exception as e:
    print(f"Error: {e}")
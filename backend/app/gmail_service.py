import os
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    """Authenticate and return the Gmail API service."""
    creds = None
    # The file token.json stores the user's access and refresh tokens.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Make sure 'credentials.json' is in your backend folder
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    return service

def fetch_unread_messages(limit=5):
    """Fetches unread emails and returns a list of dictionaries."""
    service = get_gmail_service()
    
    # List unread messages
    results = service.users().messages().list(userId='me', q='is:unread', maxResults=limit).execute()
    messages = results.get('messages', [])
    
    email_data = []

    if not messages:
        print("No new messages found.")
        return []

    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        
        # Extract headers
        headers = msg['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown Sender')
        date = next((h['value'] for h in headers if h['name'] == 'Date'), 'Unknown Date')

        # Extract Snippet (Body preview)
        snippet = msg.get('snippet', '')

        email_data.append({
            "id": message['id'],
            "sender": sender,
            "subject": subject,
            "received_at": date,
            "snippet": snippet
        })

    return email_data
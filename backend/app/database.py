from typing import List, Dict, Any

class SimpleDatabase:
    def __init__(self):
        # This acts as our "storage" while the app is running
        self.emails: List[Dict[str, Any]] = []

    def save_email(self, email_record: Dict[str, Any]):
        """Saves a processed email to the list."""
        # Check if email already exists to avoid duplicates
        if not any(e['id'] == email_record['id'] for e in self.emails):
            self.emails.append(email_record)

    def get_all_emails(self) -> List[Dict[str, Any]]:
        """Returns all stored emails."""
        return self.emails

# Initialize the 'db' variable that other files are trying to import
db = SimpleDatabase()
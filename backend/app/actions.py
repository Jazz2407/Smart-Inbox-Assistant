import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path(__file__).resolve().parent.parent / "data" / "action_logs.json"


def log_action(subject: str, action: str, status: str):
    LOG_FILE.parent.mkdir(exist_ok=True)

    if LOG_FILE.exists():
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append({
        "subject": subject,
        "action": action,
        "status": status,
        "timestamp": datetime.now().isoformat()
    })

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2)


def execute_action(subject: str, approved: bool, action: str):
    if approved:
        status = "approved"
    else:
        status = "rejected"

    log_action(subject, action, status)

    return {
        "subject": subject,
        "action": action,
        "status": status
    }

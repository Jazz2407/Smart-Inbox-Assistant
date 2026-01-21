from pydantic import BaseModel, Field
from typing import Literal, Optional, List

# The structure the AI must return
class SmartEmailAnalysis(BaseModel):
    category: Literal["Work", "Personal", "Newsletter", "Security", "Spam"]
    priority: Literal["High", "Medium", "Low"]
    summary: str = Field(..., description="A 1-sentence summary of the email")
    suggested_action: Literal["Reply", "Archive", "Create Task", "None"]
    action_detail: Optional[str] = Field(None, description="Draft reply text or task name")

# The structure your Frontend will receive
class EmailResponse(BaseModel):
    id: str
    sender: str
    subject: str
    snippet: str
    received_at: str
    analysis: Optional[SmartEmailAnalysis] = None # It might be None if not processed yet
from pydantic import BaseModel
from typing import Optional

class ChatLog(BaseModel):
    user_id: str
    request_time: Optional[str] = None
    content: str
    sender_type: str = "user"
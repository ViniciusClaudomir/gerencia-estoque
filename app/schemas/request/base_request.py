from pydantic import BaseModel
from typing import Optional

class BaseRequest(BaseModel):
    content: str
    thread_id: Optional[str] = None
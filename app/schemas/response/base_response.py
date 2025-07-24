from pydantic import BaseModel
from typing import Optional

class BaseResponse(BaseModel):
    thread_id: Optional[str] = None
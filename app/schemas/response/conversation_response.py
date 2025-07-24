from app.schemas.response.base_response import BaseResponse

class ConversationResponse(BaseResponse):
    content: str = ''
from fastapi import APIRouter

from app.schemas.request.user_message import UserMessage
from app.schemas.response.conversation_response import ConversationResponse

from app.domain.models.warehouse_domain import WarehouseDomain

router = APIRouter(prefix='/conversation', tags=['Conversation'])

@router.post("/", response_model=ConversationResponse)
def conversation(request: UserMessage):
    warehouseDomain = WarehouseDomain()
    return warehouseDomain.process_message(request)


from app.core.i18n import i18n
from app.core.logger import logger


from app.schemas.request.user_message import UserMessage
from app.schemas.response.conversation_response import ConversationResponse

from app.infrastructure.external_services.langgraph_warehouse import WarehouseGraphService

i18nimpl = i18n()

class WarehouseDomain:

    def __init__(self) -> 'WarehouseDomain':
        self.warehouse = WarehouseGraphService()
        
    def process_message(self, message=UserMessage) -> ConversationResponse | Exception:
        
        user_message = message.content
        thread_id = message.thread_id
       
        response = self.warehouse.process_message(content=user_message, thread_id=thread_id)
        return response
       
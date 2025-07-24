from fastapi import FastAPI
from app.api.v1.endpoints import conversation

app = FastAPI()
app.include_router(conversation.router)



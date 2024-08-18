from fastapi import APIRouter
from app.models import ChatLog

router = APIRouter()

# 유저 채팅송신 API
@router.post("/", response_model=ChatLog)
def post_user_chat_log(log: ChatLog):

    return "Hello Post"
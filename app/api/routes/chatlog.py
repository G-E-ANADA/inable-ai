from fastapi import APIRouter,Query
from starlette.responses import StreamingResponse

from app.core.ai import AI, AI_CLAUDE_MODEL
from app.models import ChatLog
import os

router = APIRouter()

@router.post("/", response_model=ChatLog,summary="유저 채팅송신 API")
def post_user_chat_log(log: ChatLog):

    return "Hello Post"

@router.get("/{user_id}/ai",summary="AI응답수신 API")
async def sse_endpoint(
        user_id,query: str = Query(...)):

    ai = AI(
            AI_CLAUDE_MODEL()
            , 2048
            , 0
            , os.environ["BEDROCK_REGION"]
            , True)

    return StreamingResponse(ai.run_gen_ai(query), media_type="text/event-stream")

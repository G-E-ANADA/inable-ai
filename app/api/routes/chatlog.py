from fastapi import APIRouter,Query
from starlette.responses import StreamingResponse

from app.core.ai import AI, AI_CLAUDE_MODEL
from app.models import ChatLog
import os

import httpx
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

    data = await fetch_data()
    job_posts = data.get("job_posts", [])

    summary = [
        {"회사명": post["busplaName"],
         "회사주소": post["compAddr"],
         "고용유형": post["empType"],
         "입사형태": post["enterType"],
         "직종": post["jobNm"],
         "등록기관": post["regagnName"],
         "경력": post["reqCareer"],
         "학력": post["reqEduc"],
         "급여": post["salary"],
         "양손사용정상여부": post["envBothHands"],
         "시각정상여부": post["envEyesight"],
         "근력": post["envLiftPower"],
         "청각정상여부": post["envLstnTalk"],
         "지체장애여부": post["envStndWalk"],
         "근무지역": post["searchRegion"],
         "직업카테고리": post["searchJobCategory"],
         "지체장애여부": post["envStndWalk"]
         } for post in job_posts]  # 예시로 5개만 추출
    # print(summary)

    return StreamingResponse(ai.run_gen_ai(query,summary), media_type="text/event-stream")


async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8001/job_posts/")# 로컬의 8001번 포트에서 데이터를 가져옴
        response.raise_for_status()# 응답이 성공적이지 않으면 예외를 발생시킴
        data = response.json()# 가져온 데이터를 JSON 형태로 반환

    return data# 데이터를 처리하거나 반환


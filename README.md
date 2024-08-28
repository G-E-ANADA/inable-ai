# inable-ai

--- 
# 기술스택
- AWS - Bedrock
- Fastapi
- Langchain
- MongoDB
- SSE

--- 
## 1.시스템 구조도(스크린샷 첨부 예정)
...

--- 
## 2.API 명세(스크린샷 첨부 예정)
- localhost:8000/docs

--- 
## 3.실행
- 패키지추가 및 가상환경 설정
```bash
pip3 install poetry
poetry install # 권한문제 발생 시 sudo -H pip3 install poetry
poetry shell
# 로컬실행
poetry run uvicorn app.main:app --reload
```

--- 
## 4.배포방법
- 로컬환경
   - 직접실행 (poetry run uvicorn app.main:app --reload)
- 운영환경
   - AWS서버자원 사용
   - 도커라이징(ai_api)
   - 도커파일 이미지빌드 -> 컨테이너 실행

---
## 5.핵심 라이브러리
### 5.1.Langchain
- LLM 생성 & 취합된 LLM데이터 파라미터화(유저쿼리+프롬프트+추가데이터)
- XML 태그를 함께 사용하여 프롬프트와 응답을 구조화하여 명확성을 높임

### 5.2.SSE(StreamingResponse)
- 챗봇응답을 스트림으로 반환하기위한 라이브러리
- SSE형식으로 응답을 구현
- 이에따라 챗봇은 AI응답을 실시간으로 클라이언트에 내려줄 수 있다.
- 클라이언트앱은 실시간으로 받은 데이터를 한글자씩 찍어 줄 수 있다.
![image](https://github.com/user-attachments/assets/bc82abd1-82ba-4dcd-97aa-6b4156da45d3)

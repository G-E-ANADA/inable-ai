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

---
## 6.LLM
- Claude 3 Haiku
- 사용근거
   - 클로드 제품군 중 제일 빠르고 컴팩트
   - 챗봇에 적합 > 즉각적인 반응성과 인간 상호작용을 모방하는 원활한 생성형 인공 지능(AI) 경험을 위해 설계됨
   - 저렴한 비용 > 인풋토큰 100만개 당 0.25달러, 아웃풋토큰 100만개당 1.25달러
      - ![image](https://github.com/user-attachments/assets/b9120cfc-6479-4b50-b0da-5fc0701b347e) 
   - 타 모델 대비 성능도 준수
      - ![image](https://github.com/user-attachments/assets/2c77a483-dd63-4eac-bc62-1b6e329e389d) 

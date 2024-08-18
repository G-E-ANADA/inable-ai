# inable-ai

--- 

inable프로젝트의 프론트엔드어플리케이션 레포입니다.

## tech stack
- bedrock
- fastapi
- langchain

## Api docs
- localhost:8000/docs

## Run
### 패키지추가 및 가상환경 설정
```bash
pip3 install poetry
poetry install # 권한문제 발생 시 sudo -H pip3 install poetry
poetry shell
# 로컬실행
poetry run uvicorn app.main:app --reload
```
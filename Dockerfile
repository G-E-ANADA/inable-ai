FROM python:3.12

# 작업 디렉토리 설정
WORKDIR /code

# 시스템 종속성 설치
RUN apt-get update

# Pipenv 설치
RUN pip install poetry

# pyproject.toml과 poetry.lockf를 복사
COPY ./pyproject.toml /code/
COPY ./poetry.lock /code/

# 종속성 설치
RUN poetry install --no-dev --no-root

# 애플리케이션 코드 복사
COPY ./app /code/app

# 컨테이너 시작 명령어 설정
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

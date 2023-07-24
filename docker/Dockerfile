FROM python:3.9

WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY . .

CMD ["poetry", "run", "uvicorn", "my_finance.main:app", "--host", "0.0.0.0", "--port", "80"]

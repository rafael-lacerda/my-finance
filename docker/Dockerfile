FROM python:3.9

WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY . .

CMD ["bash", "scripts/entrypoint.sh"]

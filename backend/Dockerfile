FROM python:3.11-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR app/
COPY . .

RUN pip install poetry
RUN poetry install --no-root --no-interaction --no-ansi --only main

EXPOSE 8000
CMD poetry run uvicorn --host 0.0.0.0 pokeapp.app:app

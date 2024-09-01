#FROM python:3.11-slim
#ENV POETRY_VIRTUALENVS_CREATE=false
#
#WORKDIR app/
#COPY . .
#
#RUN python -m pip install --upgrade pip && pip install pipx && pipx ensurepath
#RUN pipx install poetry
#ENV PATH="/root/.local/bin:$PATH"
#
#COPY pyproject.toml poetry.lock ./
#
#RUN poetry install --no-root --no-interaction --no-ansi --only main
#
#EXPOSE 8000
#
#CMD poetry run uvicorn --host 0.0.0.0 pokeapp.app:app

FROM python:3.11-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR app/
COPY . .

RUN pip install poetry
RUN poetry install --no-root --no-interaction --no-ansi --only main

EXPOSE 8000
CMD poetry run uvicorn --host 0.0.0.0 pokeapp.app:app

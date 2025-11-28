FROM python:3.13-alpine
WORKDIR /app

COPY *.py pyproject.toml .
COPY ./barcodes ./barcodes
COPY ./services ./services
COPY ./compressors ./compressors
COPY ./contracts ./contracts
COPY ./factories ./factories
COPY ./imaging ./imaging
COPY ./services ./services

RUN python -m pip install uv
RUN uv sync

ENTRYPOINT uv run gunicorn --bind 0.0.0.0:8080 main:app

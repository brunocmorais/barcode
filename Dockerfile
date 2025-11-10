FROM python:3.13-alpine
WORKDIR /app

COPY *.py pyproject.toml .
COPY ./barcodes ./barcodes

RUN python -m pip install uv
RUN uv sync

ENTRYPOINT uv run gunicorn --bind 0.0.0.0:8080 main:app
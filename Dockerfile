FROM astral/uv:python3.13-alpine
WORKDIR /app

COPY pyproject.toml ./
COPY ./src ./src

CMD uv run gunicorn --bind 0.0.0.0:80 --chdir src main:app

EXPOSE 80

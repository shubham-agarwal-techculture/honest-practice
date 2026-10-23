FROM python:3.12-slim-bookworm

# uv is the installer used in development as well, so the image resolves the
# same lockfile a developer does.
COPY --from=ghcr.io/astral-sh/uv:0.9.16 /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock README.md ./
COPY src ./src

RUN uv sync --frozen --no-dev

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    HP_API_HOST=0.0.0.0 \
    HP_API_PORT=8000

EXPOSE 8000

CMD ["uvicorn", "honest_practice.api.app:app", "--host", "0.0.0.0", "--port", "8000"]

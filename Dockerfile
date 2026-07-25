FROM python:3.11-slim

LABEL org.opencontainers.image.title="Northwind Logistics"
LABEL org.opencontainers.image.description="Northwind delivery tracking service"
LABEL org.opencontainers.image.source="https://github.com/Yemane1426/northwind-logistics-devops"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

WORKDIR /app

RUN useradd \
    --create-home \
    --uid 10001 \
    --shell /usr/sbin/nologin \
    appuser

COPY requirements.txt .

RUN python -m pip install \
    --no-cache-dir \
    --disable-pip-version-check \
    -r requirements.txt

COPY --chown=appuser:appuser app ./app
COPY --chown=appuser:appuser run.py ./run.py

USER appuser

EXPOSE 8000

HEALTHCHECK \
    --interval=30s \
    --timeout=5s \
    --start-period=5s \
    --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=3)"

CMD ["python", "-m", "app"]
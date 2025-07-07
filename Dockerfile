FROM python:3.9-slim

WORKDIR /app

COPY send_webhook.py .

ENTRYPOINT ["python", "/app/send_webhook.py"] 
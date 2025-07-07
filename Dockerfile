FROM python:3.10-slim

WORKDIR /app

COPY send_webhook.py .

ENTRYPOINT ["python", "send_webhook.py"] 
ARG BASE_IMAGE=python:3.9-slim
FROM ${BASE_IMAGE}

WORKDIR /app

COPY send_webhook.py .

ENTRYPOINT ["python", "/app/send_webhook.py"] 
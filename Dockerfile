FROM python:3.11-alpine

RUN mkdir -p /opt/applications/larixon

RUN apk update && \
    apk add --no-cache build-base && \
    apk add --no-cache libffi-dev

WORKDIR /opt/applications/larixon

COPY . .

RUN chmod -R 644 entrypoints/* && \
    chmod +x entrypoints/* && \
    python3 -m pip install -r requirements.txt
   
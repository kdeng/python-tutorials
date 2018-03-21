FROM python:3.6.4

LABEL developer="Kefeng Deng"

RUN mkdir -p /app

WORKDIR /app

COPY ./dist/ /app

EXPOSE 8080
ENTRYPOINT python main.py


FROM python:3.6-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirement.txt && make migrate && make compile

CMD make run
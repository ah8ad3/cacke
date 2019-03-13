FROM python:3.6-alpine

WORKDIR /app

COPY . .

RUN apk add gettext

RUN pip install -r requirement.txt && python manage.localy.py migrate && python manage.localy.py compilemessages

CMD python manage.localy.py runserver

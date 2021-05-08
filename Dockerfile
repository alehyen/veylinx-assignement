FROM python:3.8.3-alpine
WORKDIR /home/app/web

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev zlib-dev


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn

# folder to collect static files
RUN mkdir -p /home/app/staticfiles

COPY . .

ENTRYPOINT ["./entrypoint.sh"]
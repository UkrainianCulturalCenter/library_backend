FROM python:3.12-alpine3.19
LABEL maintainer="Kostiantyn Zivenko <kos.zivenko@gmail.com>"

RUN apk update

RUN addgroup -S app && adduser -S app -G app
USER app

# Инициализация проекта
WORKDIR /home/app/app

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt ./
RUN  pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
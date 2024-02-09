FROM python:3.12-alpine3.19
LABEL maintainer="Kostiantyn Zivenko <kos.zivenko@gmail.com>"

RUN apk update && \
    addgroup -S app && \
    adduser -S app -G app

# Инициализация проекта
WORKDIR /home/app/app

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY --chown=app:app requirements.txt ./
RUN  pip install -r requirements.txt
USER app
COPY --chown=app:app . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
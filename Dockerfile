FROM python:3.5
LABEL maintainer mlabouardy

COPY requirements.txt /app
ADD app /

WORKDIR /app

EXPOSE $PORT

CMD python app.py

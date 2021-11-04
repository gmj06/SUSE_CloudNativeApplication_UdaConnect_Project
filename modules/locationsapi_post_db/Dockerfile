FROM python:3.7-alpine
# RUN mkdir /backend

WORKDIR . 
# /backend

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python","locations_kafka_db.py"]

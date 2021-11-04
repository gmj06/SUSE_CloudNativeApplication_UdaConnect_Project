from kafka import KafkaConsumer
from sqlalchemy import create_engine
from geoalchemy2.functions import ST_AsText, ST_Point
import os

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]
TOPIC_NAME= "locations-topic"
KAFKA_SERVER= "kafka-service:9092"


SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print(f"SQLALCHEMY_DATABASE_URI - {SQLALCHEMY_DATABASE_URI}")
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=[KAFKA_SERVER])

print("Kafka Consumer Started...")

def kafka_to_db(location):
    db = create_engine(SQLALCHEMY_DATABASE_URI)
    connection = db.connect()

    insert = "INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}))" \
        .format(location["person_id"], int(location["latitude"]), int(location["longitude"]))

    print(insert)
    connection.execute(insert)



for location in consumer:
    location_data = location.value.decode("utf-8")
    print(f"Topic Name={location.topic},location={location_data}")
    kafka_to_db(location_data)
    print("Successfully location created...")

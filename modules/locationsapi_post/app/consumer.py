from kafka import KafkaConsumer


TOPIC_NAME = 'locations-topic'
KAFKA_URL='kafka-service:9092'

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=[KAFKA_URL])
# consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    print (message)

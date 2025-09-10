from kafka import KafkaConsumer
import json

class Subscriber:
    def __init__(self,topic):
        self.consumer = KafkaConsumer(topic,
            value_deserializer=lambda m: json.loads(m.decode('ascii')),
            bootstrap_servers=["broker:9092"],
            consumer_timeout_ms=5000)
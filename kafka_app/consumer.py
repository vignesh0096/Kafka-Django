from kafka import KafkaConsumer
import json


def consumer1():
    topic = str(input('Enter topic name (culture/us_news/comedy/world_news) :')).upper()
    consumer = KafkaConsumer(topic,bootstrap_servers=['localhost:9092'],
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')),
                             auto_offset_reset='earliest')

    for message in consumer:
        print(f'content about {topic}')
        print(message.value)

import json
import time
from kafka import KafkaProducer
from json import dumps


def producer1():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x: dumps(x).encode('utf-8'))
    with open(r"data.json", 'r') as a:
        data = json.load(a)
    for datas in data:
        producer.send('data', value=datas)
        print('data added')







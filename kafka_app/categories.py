from kafka import KafkaConsumer,KafkaProducer
import json


def categories():
    consumer = KafkaConsumer('data',bootstrap_servers=['localhost:9092'],
                             value_deserializer=lambda y: json.loads(y.decode('utf-8')),
                             auto_offset_reset='earliest')

    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda z: json.dumps(z).encode('utf-8'))

    for message in consumer:
        if message.value['category'] == "U.S. NEWS":
            print('Data of US_NEWS')
            producer.send('US_NEWS',value=message)
        elif message.value['category'] == 'CULTURE & ARTS':
            print('Data of CULTURE & ARTS')
            producer.send('CULTURE',value=message)
        elif message.value['category'] == 'COMEDY':
            print('Data of COMEDY')
            producer.send('COMEDY',value=message)
        elif message.value['category'] == 'WORLD NEWS':
            print('Data of WORLD_NEWS')
            producer.send('WORLD_NEWS',value=message)

    producer.close()
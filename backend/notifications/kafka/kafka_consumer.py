from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('flight-status',
                         bootstrap_servers='localhost:9092',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
    print(message.value)
    # Process flight update message

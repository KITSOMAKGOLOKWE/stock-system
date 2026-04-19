from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'stock-prices',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Listening for stock data...")

for message in consumer:
    data = message.value

    print("\nReceived:")
    print("Stock:", data["stock"])
    print("Price:", data["price"])
    print("Time:", data["timestamp"])
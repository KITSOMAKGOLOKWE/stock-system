from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

stocks = ["AAPL", "TSLA", "GOOG"]

while True:
    data = {
        "stock": random.choice(stocks),
        "price": round(random.uniform(100, 300), 2),
        "timestamp": time.time()
    }

    producer.send("stock-prices", data)
    print("Sent:", data)

    time.sleep(2)
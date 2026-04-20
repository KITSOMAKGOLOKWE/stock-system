# Kafka Stock Streaming System

## Description
This project simulates real-time stock price streaming using Apache Kafka.

## Technologies
- Docker
- Apache Kafka
- Python

## How to Run
1. docker compose up -d
2. Create topic:
   docker exec -it kafka kafka-topics --create --topic stock-prices --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
3. Run consumer:
   python consumer.py
4. Run producer:
   python producer.py

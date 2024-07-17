import json
from kafka import KafkaProducer
from datetime import datetime
import time
import random

# Kafka configuration
kafka_bootstrap_servers = "172.31.17.38:9092"  # Update with your Kafka bootstrap server
kafka_topic = "user-activity"

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers=kafka_bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# List of possible event types
event_types = ["login", "logout", "purchase", "add_to_cart"]

# Function to generate a random event
def generate_event():
    return {
        "event_time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
        "event_type": random.choice(event_types)
    }

# Produce messages to Kafka
def produce_messages():
    while True:
        event = generate_event()
        producer.send(kafka_topic, event)
        print(f"Produced event: {event}")
        time.sleep(1)  # Adjust the delay as needed

    # Wait for all messages to be sent
    producer.flush()

if __name__ == "__main__":
    produce_messages()
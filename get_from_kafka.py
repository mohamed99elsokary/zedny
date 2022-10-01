import csv
import json
from kafka import KafkaConsumer


def write_in_csv(data):
    fieldnames = ["id", "title", "country", "city", "latitude", "longitude"]

    # check if file and header exist or not
    try:
        with open("data_file.csv", "r") as file:
            reader = csv.reader(file)
            row = next(reader)
            header = row[0] == fieldnames[0]
    except:
        header = False

    with open("data_file.csv", "a+", newline="") as data_file:
        writer = csv.DictWriter(data_file, fieldnames=fieldnames)
        if not header:
            writer.writeheader()
        writer.writerow(data)


def get_from_kafka():
    topic_name = "test-topic"
    consumer = KafkaConsumer(topic_name)
    for message in consumer:
        data = message.value.decode("utf-8")
        data = json.loads(data)
        print(data)
        write_in_csv(data)


get_from_kafka()

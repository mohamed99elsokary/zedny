import json

from cities_light import models as cites_models
from django.db import models
from django.db.models.signals import post_save
from kafka import KafkaProducer


class Brochure(models.Model):
    # relations
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    # fields
    brochure = models.FileField(upload_to="media/brochures/", max_length=100)

    def __str__(self):
        return self.brand.title


# Create your models here.
class Brand(models.Model):
    # relations
    country = models.ForeignKey(
        cites_models.Country,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
    )
    city = models.ForeignKey(
        cites_models.Region,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
    )
    # fields
    title = models.CharField(max_length=50)
    descreption = models.TextField()
    logo = models.ImageField(
        upload_to="media/logos/", height_field=None, width_field=None, max_length=None
    )
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# send data to kafka topic
def send_to_kafka(sender, instance, *args, **kwargs):
    # organize the data to send it to kafka
    data = {
        "id": instance.id,
        "title": instance.title,
        "country": instance.country.name,
        "city": instance.city.name,
        "latitude": instance.latitude,
        "longitude": instance.longitude,
    }
    data = json.dumps(data)
    # send to kafka
    topic_name = "test-topic"
    kafka_server = "localhost:9092"
    producer = KafkaProducer(bootstrap_servers=kafka_server)
    # send the data to kafka + encode the data first
    producer.send(topic_name, bytes(data, encoding="utf-8"))
    producer.flush()


post_save.connect(send_to_kafka, sender=Brand)

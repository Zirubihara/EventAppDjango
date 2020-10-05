import random

from django.db import models


# Create your models here.
class Event(models.Model):
    # id
    name = models.CharField(blank=False, null=False, unique=True, max_length=100, verbose_name=("Nazwa wydarzenia"))
    description = models.CharField(blank=False, null=False, max_length=500, verbose_name=("Opis wydarzenia"))
    text = models.CharField(blank=False, null=False, max_length=5000, verbose_name=("Treść ogłoszenia eventu"))
    # organizer as text at this moment
    organizer = models.CharField(blank=False, null=False, max_length=100, verbose_name=("Organizator"))
    eventDate = models.DateTimeField(blank=False, verbose_name=("Data Eventu"))
    location = models.CharField(max_length=150, verbose_name=("Lokalizacja Eventu"))

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "text": self.text,
            "likes": random.randint(0, 200),
        }

from django.db import models
import random
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    #id
    name = models.CharField(blank=True, null=True, unique=True, max_length=100)
    description = models.CharField(blank=True, null=True, max_length=500)
    text = models.CharField(blank=True, null=True, max_length=5000)

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "text": self.text,
            "likes": random.randint(0,200),
        }


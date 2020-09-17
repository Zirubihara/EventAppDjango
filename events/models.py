from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(blank=True, null=True, unique=True, max_length=100)
    description = models.CharField(blank=True, null=True, max_length=500)
    text = models.CharField(blank=True, null=True, max_length=5000)


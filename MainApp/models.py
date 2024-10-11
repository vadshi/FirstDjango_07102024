from django.db import models
from django.db.models import Manager # special for PyCharm Community


# Create your models here.

class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField() 
    description = models.TextField(max_length=200, default="Базовое описание")

    objects: Manager  # <- this annotation
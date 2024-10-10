from django.db import models
from django.db.models import Manager # special for PyCharm Community


# Create your models here.

class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField() 

    objects: Manager  # <- this annotation
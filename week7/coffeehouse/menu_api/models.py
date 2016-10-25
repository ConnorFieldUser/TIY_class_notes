from django.db import models

# Create your models here.


class Special(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.TextField()

from django.db import models

# Create your models here.


class Chirp(models.Model):
    body = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)

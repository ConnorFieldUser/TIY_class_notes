from django.db import models

# Create your models here.


class Song(models.Model):
    artist = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    lyrics = models.TextField()
    release_year = models.IntegerField()

    def __str__(self):
        return self.title

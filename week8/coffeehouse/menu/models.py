from django.db import models

# Create your models here.


class Special(models.Model):
    created_user = models.ForeignKey('auth.user')
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_times = models.DateTimeField(auto_now_add=True)
    picture = models.FileField()

from django.db import models

# Create your models here.


class Fear(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Person(models.Model):

    name = models.CharField(max_length=30)
    age = models.IntegerField()
    eye_color = models.CharField(max_length=15)
    best_friend = models.ForeignKey("self", null=True)
    fears = models.ManyToManyField(Fear)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    captain = models.ForeignKey(Person)

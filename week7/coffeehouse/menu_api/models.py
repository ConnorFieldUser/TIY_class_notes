from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=40)
    calories = models.IntegerField()


class Special(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.TextField()
    ingredients = models.ManyToManyField("menu_api.Ingredient")

    @property
    def calorie_count(self):
        return sum(self.ingredients.all().values_list("calories", flat=True))

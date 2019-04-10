from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    """Модель Рецепта"""
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=2000)
    ingred = models.TextField(max_length=200)
    image = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, models.CASCADE)
    count_views = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    rating_count = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Comment(models.Model):
    """Модель комментария"""
    text = models.TextField(max_length=2000)
    owner = models.ForeignKey(User, models.CASCADE)
    recipe = models.ForeignKey(Recipe, models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
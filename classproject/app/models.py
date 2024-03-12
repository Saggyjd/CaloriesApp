from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.FloatField()

    def __str__(self):
        return self.name
    
class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foodconsumed = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
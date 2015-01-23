from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    rating = models.FloatField(default=0.0)
    year = models.IntegerField(default=0)
    summary = models.TextField()

# Create your models here.

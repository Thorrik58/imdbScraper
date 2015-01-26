from django.db import models
from datetime import datetime

class Movie(models.Model):
    name = models.CharField(max_length=200)
    rating = models.FloatField(default=0.0)
    pubdate = models.DateField(default=datetime.now, blank=True)
    ranking = models.IntegerField(default=0)
    year = models.IntegerField(default=0)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

# Create your models here.

from turtle import title
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.title} - {self.year}'
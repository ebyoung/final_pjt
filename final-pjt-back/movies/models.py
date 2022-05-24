from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=100)
    video_key = models.CharField(max_length=100)
    recommendations = models.ManyToManyField('self')
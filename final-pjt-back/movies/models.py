from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=100)
    video_key = models.TextField()
    recommendations = models.ManyToManyField('self')


def map_movie_image_path(instance, filename):
    return f'movies/{instance.movie_id}/{filename}'


class MapMovie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to=map_movie_image_path)
    image2 = models.ImageField(upload_to=map_movie_image_path)
    image3 = models.ImageField(upload_to=map_movie_image_path)
    image4 = models.ImageField(upload_to=map_movie_image_path)
    image5 = models.ImageField(upload_to=map_movie_image_path)

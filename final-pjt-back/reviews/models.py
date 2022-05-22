from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
# from imagekit.processors import Crop


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie_title = models.CharField(max_length=100)
    content = models.TextField()
    vote = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # watch_day 고민해보기
    watch_day = models.DateField(auto_now_add=True)
    review_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    movie_poster = models.TextField()


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    re_comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='re_comments', null=True) # ??
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')

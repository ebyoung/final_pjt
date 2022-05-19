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
    watch_day = models.DateField()
    review_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    movie_poster = ProcessedImageField(
        blank=True,
        upload_to='poster_images/',
        format='JPEG',
        # processors=[Crop(1080, 1920)], # 포스터 사이즈 맞춰서
        # options={
        #     'quality': 90,
        # }
    )


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    # re_comment = models.ForeignKey(self, on_delete=models.CASCADE, related_name='re_comments') # ??
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')

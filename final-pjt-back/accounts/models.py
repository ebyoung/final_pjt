from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
# from imagekit.processors import Resize


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    introduction = models.TextField(blank=True)
    profile_image = ProcessedImageField(
        upload_to='profile_images/',
        default='profile_images/default_profile.png',
        # format='JPEG',
        # processors=[Resize(1080, 1920)],
        # options={
        #     'quality': 90,
        # }
    )

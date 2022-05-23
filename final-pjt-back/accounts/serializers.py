from rest_framework import serializers
from django.contrib.auth import get_user_model
from reviews.models import Review

class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('profile_image', )



class ProfileSerializer(serializers.ModelSerializer):

    class ReviewListSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = ('pk', 'watch_day', 'vote', 'movie_title', 'movie_poster')
    
    class FollowSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('username', 'profile_image', )

    reviews = ReviewListSerializer(read_only=True, many=True)
    followers = FollowSerializer(read_only=True, many=True)
    followings = FollowSerializer(read_only=True, many=True)
    follower_count = serializers.IntegerField(source='followers.count', read_only=True)
    following_count = serializers.IntegerField(source='followings.count', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('profile_image', 'username', 'follower_count', 'following_count', 'followers', 'followings', 'reviews', 'introduction')
from rest_framework import serializers
from .models import Review, Comment
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('profile_image', 'username',)


class CommentSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    comment_likes_count = serializers.IntegerField(source='comment_like_users.count', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('comment_like_users', 'review', 're_comment',)


class ReviewListSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    review_likes_count = serializers.IntegerField(source='review_like_users.count', read_only=True)
    review_comments_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Review
        fields = ('pk', 'movie_title', 'user', 'vote', 'content', 'review_likes_count', 'review_comments_count', 'watch_day', 'movie_poster', 'updated_at',)


class ReviewSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    review_likes_count = serializers.IntegerField(source='review_like_users.count', read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('review_like_users',)

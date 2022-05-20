from rest_framework import serializers
from .models import Review, Comment
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('profile_image', 'username', )


class CommentSerializer(serializers.ModelSerializer):

    comment_likes_count = serializers.IntegerField(source='comment_like_users.count', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('poster_image', 'user', 'vote', 'content',)


class ReviewSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, read_only=True)
    review_likes_count = serializers.IntegerField(source='review_like_users.count', read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'review_like_users',)

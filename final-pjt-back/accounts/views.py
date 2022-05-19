from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProfileSerializer

User = get_user_model()

@api_view(['GET', 'POST'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    def read_profile():
        serializer = ProfileSerializer(user)
        return Response(serializer.data)
    
    def update_profile():
        if request.user == user:
            serializer = ProfileSerializer(user, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            data = {
                'error': '자신의 프로필만 수정할 수 있습니다.',
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        return read_profile()
    elif request.method == 'POST':
        return update_profile()


@api_view(['POST'])
def follow(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    followed = False
    if request.user.is_authenticated:
        if user != request.user:
            if user.followers.filter(pk=request.user.pk).exists():
                user.followers.remove(request.user)
            else:
                user.followers.add(request.user)
                followed = True
        print(user.followers.all())
        serializer = ProfileSerializer(user)
        return Response(serializer.data)

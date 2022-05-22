from rest_framework import serializers
from .models import Movie

class MovieTitleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
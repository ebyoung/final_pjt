from rest_framework import serializers
from .models import Movie, MapMovie

class MovieTitleListSerializer(serializers.ModelSerializer):
    
    class MovieRecommendationSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = '__all__'

    recommendations = MovieRecommendationSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = '__all__'


class MapMovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MapMovie
        fields = '__all__'
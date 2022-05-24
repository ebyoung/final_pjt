from rest_framework import serializers
from .models import Movie

class MovieTitleListSerializer(serializers.ModelSerializer):
    
    class MovieRecommendationSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = '__all__'

    recommendations = MovieRecommendationSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = '__all__'
from django.shortcuts import render
from .models import Movie
from .serializers import MovieTitleListSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def movies(request):
    movies = Movie.objects.order_by('title')
    serializer = MovieTitleListSerializer(movies, many=True)
    return Response(serializer.data)


def get_data(request):
    import csv
    f = open('movie_data.csv', 'r', encoding='euc-kr')
    data_csv = csv.reader(f)
    next(data_csv, None)
    for line in data_csv:
        idx, movie_id, title, overview, poster_path, video_key = line
        Movie.objects.create(movie_id=int(movie_id), title=title, overview=overview, poster_path=poster_path, video_key=video_key)
    
    return render(request, 'hi.html')
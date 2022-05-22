from django.shortcuts import render
from .models import Movie

# Create your views here.
def get_data(request):
    import csv
    f = open('movie_data.csv', 'r', encoding='euc-kr')
    data_csv = csv.reader(f)
    next(data_csv, None)
    for line in data_csv:
        idx, movie_id, title, overview, poster_path, video_key = line
        Movie.objects.create(movie_id=int(movie_id), title=title, overview=overview, poster_path=poster_path, video_key=video_key)
    
    return render(request, 'hi.html')
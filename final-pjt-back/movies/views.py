from django.shortcuts import render
from .models import MapMovie, Movie
from .serializers import MovieTitleListSerializer, MapMovieListSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()


@api_view(['GET'])
def movies(request):
    movies = Movie.objects.order_by('title')
    serializer = MovieTitleListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def map(request):
    map_movies = MapMovie.objects.all()
    serializer = MapMovieListSerializer(map_movies, many=True)
    return Response(serializer.data)


def get_data(request):
    # 영화 데이터 csv 파일 사용시
    import csv
    f = open('movie_data_small.csv', 'r', encoding='utf-8-sig')
    data_csv = csv.reader(f)
    next(data_csv, None)

    # db에 영화 데이터를 저장
    for line in data_csv:
        idx, movie_id, title, poster_path, video_key = line
        if Movie.objects.filter(movie_id=movie_id).exists():
            continue
        Movie.objects.create(movie_id=int(movie_id), title=title, poster_path=poster_path, video_key=video_key)

    # 중복 데이터 제거: 필요없음
    # movies = {}
    # for line in data_csv:
        # idx, movie_id, title, poster_path, video_key = line
    #     movies[title] = movies.get(title, 0) + 1
    # for key, val in movies.items():
    #     if val > 1:
    #         Movie.objects.filter(title=key)[0].delete()

    # 영화 추천 데이터 json 파일 사용해 넣기
    import json
    f = open('recoms_small.json', 'r', encoding='utf-8-sig')
    data = json.load(f)
    for target_id, recom_ids in data.items():
        target = Movie.objects.get(movie_id=target_id)
        if target.recommendations.count() > 0:
            continue
        for recom_id in recom_ids:
            recom = Movie.objects.get(movie_id=recom_id)
            target.recommendations.add(recom)

    return render(request, 'hi.html')

@api_view(['GET'])
def recommendations(request):
    print(request.user)
    user = get_object_or_404(User, pk=request.user.pk)
    reviews = user.reviews.all()
    recom_list = {}
    for review in reviews:
        target = Movie.objects.get(title = review.movie_title)
        score = int(review.vote)
        recoms = target.recommendations.all()
        for recom in recoms:
            recom_list[recom.title] = recom_list.get(recom.title, 0) + score
    
    top5 = []
    for title, score in recom_list.items():
        if len(top5) < 5:
            top5.append(title)
        else:
            third = top5[-1]
            if recom_list[third] < recom_list[title]:
                top5[-1] = title
        top5.sort(key=lambda x: recom_list[x], reverse=True)
    
    top5_data = []
    for title in top5:
        movie = Movie.objects.get(title = title)
        data = {
            'movieId': movie.movie_id,
            'title': movie.title,
            'posterPath': movie.poster_path,
        }
        top5_data.append(data)
    return Response(top5_data)
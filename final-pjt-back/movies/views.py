from django.shortcuts import render
from .models import Movie
from .serializers import MovieTitleListSerializer
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


def get_data(request):
    # 영화 데이터 csv 파일 사용시
    import csv
    f = open('movie_data_small.csv', 'r', encoding='utf-8-sig')
    data_csv = csv.reader(f)
    next(data_csv, None)

    # db에 영화 데이터를 저장
    for line in data_csv:
        idx, movie_id, title, overview, poster_path, video_key = line
        Movie.objects.create(movie_id=int(movie_id), title=title, overview=overview, poster_path=poster_path, video_key=video_key)

    # 중복 데이터 제거
    # movies = {}
    # for line in data_csv:
        # idx, movie_id, title, overview, poster_path, video_key = line
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
    
    top3 = []
    for title, score in recom_list.items():
        if len(top3) < 3:
            top3.append(title)
        else:
            third = top3[-1]
            if recom_list[third] < recom_list[title]:
                top3[-1] = title
        top3.sort(key=lambda x: recom_list[x], reverse=True)
    
    top3_data = []
    for title in top3:
        movie = Movie.objects.get(title = title)
        data = {
            'movieId': movie.movie_id,
            'title': movie.title,
            'overview': movie.overview,
            'posterUrl': f'https://image.tmdb.org/t/p/w500/{movie.poster_path}',
            'videoUrl': f'https://www.youtube.com/embed/{movie.video_key}?controls=0&rel=0&autoplay=1&mute=1&loop=1&playlist={movie.video_key}',
        }
        top3_data.append(data)
    return Response(top3_data)
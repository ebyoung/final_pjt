import requests
import pandas as pd

# 요청 보내는 함수 정의
def get_request(path, **kwargs):
    url = 'https://api.themoviedb.org/3'
    params = {
        'api_key':'7e70884f7539c7fbdc8e1f31d3f488cf',
        'language':'ko-KR'
    }
    
    params.update(kwargs)
    
    response = requests.get(url+path, params=params)
    data = response.json()

    return data

fields = ['id', 'title', 'overview', 'poster_path', 'video_key']
result_data = []
for i in range(1, 101):
    if not i % 10:
        print('▮', end='')
    movies = get_request('/movie/popular', page=i).get('results')
    for movie in movies:
        id = movie['id']
        video = get_request(f'/movie/{id}/videos')
        if video.get('results'):
            result = [id, movie['title'], movie['overview'], movie['poster_path'], video['results'][0]['key']]
            result_data.append(result)


# `https://www.youtube.com/embed/${state.videoKey}?controls=0&rel=0&autoplay=1&mute=1&loop=1&playlist=${state.videoKey}`

df = pd.DataFrame(
    result_data,
    columns=fields)
df.to_csv("movie_data.csv", encoding='euc-kr')

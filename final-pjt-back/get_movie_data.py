# `https://www.youtube.com/embed/${state.videoKey}?controls=1&rel=0&autoplay=1&mute=1&loop=1&playlist=${state.videoKey}`
from operator import index
import requests
import pandas as pd
from pprint import pprint
import json


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

# 영화데이터 받아와 csv로 저장
# fields = ['id', 'title', 'poster_path', 'video_key']
# result_data = set()
# for path in ['now_playing', 'popular', 'top_rated']:
#     for i in range(1, 6):
#         movies = get_request(f'/movie/{path}', page=i).get('results')
#         for movie in movies:
#             id = movie['id']
#             video = get_request(f'/movie/{id}/videos')
#             if video.get('results'):
#                 poster = 'https://image.tmdb.org/t/p/w500/' + movie['poster_path']
#                 video = f"https://www.youtube.com/embed/{video['results'][0]['key']}?controls=1&rel=0&mute=1&autoplay=1&loop=1&playlist={video['results'][0]['key']}"
#                 result = (id, movie['title'], poster, video)
#                 result_data.add(result)
#     print('■')
# #
# df = pd.DataFrame(
#     list(result_data),
#     columns=fields)
# df.to_csv("movie_data_small.csv", encoding='utf-8-sig')


# 추천 영화 정보 받아오기
df = pd.read_csv('movie_data_small.csv', encoding='utf-8-sig', index_col=0)
id_col = set(df['id'])
# recoms = {}
# i = 0
# for id in id_col:
#     i += 1
#     print(round(i/len(id_col)*100, 2), '%')
#     recom_list =  []
#     page = 1
#     while len(recom_list) < 7:
#         results = get_request(f'/movie/{id}/recommendations', page=page).get('results')
#         for result in results:
#             if result['id'] in id_col and result['id'] not in recom_list and result['id'] != id:
#                 recom_list.append(result['id'])
#         page += 1
#         if page > 10:
#             break
#
#     page = 1
#     while len(recom_list) < 7:
#         results = get_request(f'/movie/{id}/similar', page=page).get('results')
#         for result in results:
#             if result['id'] in id_col and result['id'] not in recom_list:
#                 recom_list.append(result['id'])
#         page += 1
#         if page > 10:
#             break
#
#     recoms[id] = recom_list
#
#
# with open('recoms_small.json', 'w', encoding='utf-8-sig') as file:
#     json.dump(recoms, file, indent=2)


# 라라랜드를 찾아서
# detail = get_request(f'/movie/313369')
# pprint(detail)

id = 313369
recom_list = []
page = 1
while len(recom_list) < 7:
    results = get_request(f'/movie/{id}/recommendations', page=page).get('results')
    for result in results:
        if result['id'] in id_col and result['id'] not in recom_list and result['id'] != id:
            recom_list.append(result['id'])
    page += 1
    if page > 10:
        break

page = 1
while len(recom_list) < 7:
    results = get_request(f'/movie/{id}/similar', page=page).get('results')
    for result in results:
        if result['id'] in id_col and result['id'] not in recom_list:
            recom_list.append(result['id'])
    page += 1
    if page > 10:
        break
pprint(recom_list)
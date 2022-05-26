from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movies),
    path('map/', views.map),
    path('get_data/', views.get_data),
    path('recommendations/', views.recommendations),
]
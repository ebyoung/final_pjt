from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('get_data', views.get_data),
]
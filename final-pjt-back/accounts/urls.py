from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<username>/', views.profile),
    path('profile/', views.social),
    path('follow/<username>/', views.follow),
    path('profile-path/<username>/', views.profile_path),
]

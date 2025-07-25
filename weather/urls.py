"""URL configuration for weather app"""
from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.weather_view, name='index'),
    path('refresh/', views.refresh_weather, name='refresh'),
    path('weather-by-location/', views.weather_by_location, name='weather_by_location'),
]

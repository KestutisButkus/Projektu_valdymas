from django.urls import path
from . import views

urlpatterns = [
    path('', views.city_distance_view, name='distance'),  # Pagrindinis "distance" programos maršrutas
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_list, name='film_list'),  # Список фильмов
    path('add/', views.add_film, name='add_film'),  # Добавить фильм
]

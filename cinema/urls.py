from django.urls import path

from cinema.views import movie_list, movie_detail

app_name = "cinema"

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:movie_id>/", movie_detail, name="movie-detail"),
]

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import MoviesViewSet, CinemaViewSet, MovieFormatViewSet, ShowTimesViewSet

router = routers.SimpleRouter()
router.register("cinema_viewset", CinemaViewSet, basename="cinema")
router.register("movie_format_viewset", MovieFormatViewSet, basename="movie_format")
router.register("movies_viewset", MoviesViewSet, basename="movies")
router.register("showtime_viewset", ShowTimesViewSet, basename="showtimes")


urlpatterns = [
    path("", include(router.urls)),
]
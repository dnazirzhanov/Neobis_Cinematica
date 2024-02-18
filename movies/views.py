from datetime import datetime
from django.db.models import Subquery
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAdminOrReadOnly
from .models import Cinemas, Movie, ShowTimes, MovieFormat, AgeLimit, Genre
from .serializers import MovieSerializers, CinemasSerializers, MovieFormatSerializers, ShowTimesSerializers


class MoviesViewSet(ModelViewSet):
    serializer_class = MovieSerializers
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        current_time = datetime.today().date()
        movies = Movie.objects.filter(date_start__gte=current_time, date_end__lte=current_time)
        return movies


class MovieFormatViewSet(ModelViewSet):
    queryset = MovieFormat.objects.all()
    serializer_class = MovieFormatSerializers
    permission_classes = [IsAdminOrReadOnly]


class CinemaViewSet(ModelViewSet):
    serializer_class = CinemasSerializers
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        current_time = datetime.today().date()
        cinemas = Cinemas.objects.filter(day_start__gte=current_time, day_end__lte=current_time)
        return cinemas


class ShowTimesViewSet(ModelViewSet):
    serializer_class = ShowTimesSerializers
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        current_time = datetime.today()
        movies = Movie.objects.filter(date_end__gte=current_time.date())
        showtimes = ShowTimes.objects.filter(movie__in=Subquery(movies.values("id")))
        active_showtimes = showtimes.objects.filter(session_start__gte=current_time.time())
        return active_showtimes
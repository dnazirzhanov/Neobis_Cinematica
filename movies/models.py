from django.db import models
from room.models import Room


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AgeLimit(models.Model):
    age = models.CharField(max_length=3)

    def __str__(self):
        return self.age

class MovieFormat(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    allowed_age = models.ForeignKey(AgeLimit, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()
    movie_format = models.ForeignKey(MovieFormat, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Cinemas(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=300)
    day_start = models.DateField()
    day_end = models.DateField()
    contact_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class ShowTimes(models.Model):
    session_start = models.TimeField()
    session_end = models.TimeField()
    cinema = models.ForeignKey(Cinemas, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rooms = models.ForeignKey(Room, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.movie}'s sessions in {self.cinema} {self.rooms} will start at {self.session_start} and end at {self.session_start}"

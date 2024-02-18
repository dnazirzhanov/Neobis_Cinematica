from rest_framework.serializers import ModelSerializer

from .models import Cinemas, Movie, ShowTimes, MovieFormat


class CinemasSerializers(ModelSerializer):
    class Meta:
        model = Cinemas
        fields = "__all__"

class MovieFormatSerializers(ModelSerializer):
    class Meta:
        model = MovieFormat
        fields = "__all__"


class MovieSerializers(ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class ShowTimesSerializers(ModelSerializer):
    class Meta:
        model = ShowTimes
        fields = "__all__"
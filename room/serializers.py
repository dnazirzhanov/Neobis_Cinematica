from rest_framework.serializers import ModelSerializer
from .models import Room, RoomCategory, Seats

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class RoomCategorySerializer(ModelSerializer):
    class Meta:
        model = RoomCategory
        fields = "__all__"


class SeatsSerializer(ModelSerializer):
    class Meta:
        model = Seats
        fields = "__all__"

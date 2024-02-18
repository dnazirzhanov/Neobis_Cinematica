from rest_framework.viewsets import ModelViewSet
from .models import Room, RoomCategory, Seats
from .serializers import RoomSerializer, RoomCategorySerializer, SeatsSerializer
from .permissions import IsAdminOrReadOnly

class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminOrReadOnly]


class RoomCategoryViewSet(ModelViewSet):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomCategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class SeatsViewSet(ModelViewSet):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer
    permission_classes = [IsAdminOrReadOnly]


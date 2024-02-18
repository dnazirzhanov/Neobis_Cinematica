from rest_framework.viewsets import ModelViewSet
from .models import User, Feedback, BonusCard
from .serializers import UserSerializer, FeedbackSerializer, BonusCardSerializer
from .permissions import UserPermission, IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]


class FeedbackViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BonusCardViewSet(ModelViewSet):
    queryset = BonusCard.objects.all()
    serializer_class = BonusCardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
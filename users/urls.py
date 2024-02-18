from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FeedbackViewSet, BonusCardViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'feedbacks', FeedbackViewSet, basename='feedback')
router.register(r'clubcards', BonusCardViewSet, basename='bonuscard')

urlpatterns = [
    path("", include(router.urls)),
]
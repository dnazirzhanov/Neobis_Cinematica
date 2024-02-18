from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import RoomViewSet, RoomCategoryViewSet, SeatsViewSet


router = routers.SimpleRouter()
router.register("room_viewset", RoomViewSet)
router.register("room_category_viewset", RoomViewSet)
router.register("seats_viewset", RoomViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
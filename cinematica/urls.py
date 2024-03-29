from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls')),
    path('', include('room.urls')),
    path('', include('order.urls')),
    path('', include('users.urls')),
]

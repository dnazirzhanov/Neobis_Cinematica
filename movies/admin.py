from django.contrib import admin
from .models import Cinemas, Movie, ShowTimes, MovieFormat, AgeLimit, Genre


admin.site.register(Cinemas)
admin.site.register(Movie)
admin.site.register(ShowTimes)
admin.site.register(MovieFormat)
admin.site.register(AgeLimit)
admin.site.register(Genre)




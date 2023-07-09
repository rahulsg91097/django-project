from .models import Movie
from django.contrib import admin

class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Movie, MovieAdmin)
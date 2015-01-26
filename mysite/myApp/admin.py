from django.contrib import admin
from myApp.models import Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'ranking', 'year', 'pubdate')
    search_fields = ['name']
    list_per_page = 250
    ordering = ('-ranking',)

admin.site.register(Movie, MovieAdmin)

from django.contrib import admin
from movies.models import Category, Keyword, Movie


admin.site.register(Category)
admin.site.register(Keyword)
admin.site.register(Movie)


from django.urls import path, include
from rest_framework import routers
from . import views

app_name = "movies"

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'keyword', views.KeywordViewSet)
router.register(r'movie', views.MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('page-movies', views.HomePage.as_view(), name='home_movies'),

]
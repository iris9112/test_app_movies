from django.urls import path, include

from rest_framework import renderers
from rest_framework import routers

from . import views

app_name = "movies"

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'keyword', views.KeywordViewSet)
router.register(r'movie', views.MovieViewSet)

movie2_list = views.MovieViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
movie2_detail = views.MovieViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('', include(router.urls)),
    path('page-movies', views.HomePage.as_view(), name='home_movies'),
    path('api-movies', views.ApiPage.as_view(), name='api_movies'),
    path('movie2/', movie2_list, name='movie2-list'),
    path('movie2/<int:pk>/', movie2_detail, name='movie2-detail'),

]



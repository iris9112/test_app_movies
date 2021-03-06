from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.response import Response
from rest_framework import viewsets

from movies.serializers import CategorySerializer, KeywordSerializer, MovieSerializer
from movies.models import Category, Keyword, Movie


class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'movies/movies_page.html'


class ApiPage(LoginRequiredMixin, TemplateView):
    template_name = 'movies/api_movies.html'    

    
class CategoryViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer


class KeywordViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Keyword.objects.all().order_by('name')
    serializer_class = KeywordSerializer


class MovieViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('title')
    serializer_class = MovieSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


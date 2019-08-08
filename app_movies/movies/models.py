from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Name category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Keyword(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='key Word')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    year = models.IntegerField(default=1900, verbose_name='Year')
    summary = models.CharField(max_length=500, verbose_name='Plot Summary')
    categories = models.ManyToManyField(Category, verbose_name='Categories')
    keywords = models.ManyToManyField(Keyword, verbose_name='Keywords')
    poster = models.CharField(max_length=500, null=True, blank=True, verbose_name='url_poster')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
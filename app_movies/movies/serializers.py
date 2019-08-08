from rest_framework import serializers

from movies.models import Category, Keyword, Movie


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class KeywordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Keyword
        fields = ['id', 'name']


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    #categories = CategorySerializer(many=True)
    keywords = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    categories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )

    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'summary', 'poster', 'categories', 'keywords']
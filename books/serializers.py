from django.contrib.auth.models import User
from rest_framework import serializers

from books.models import Book, Author


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SlugRelatedField(slug_field='id', queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'page_count', 'url']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'birth_year', 'bio', 'url']
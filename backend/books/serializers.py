from books.models import Book, Author, Genres, Publisher
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "year", "num_of_pages", "price", "url", "images", "annotation", "book_id"]
        extra_kwargs = {"title": {'required': True, 'allow_null': False},
                        "year": {'required': True, 'allow_null': False},
                        "images": {'required': True, 'allow_null': False}}


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genres
        fields = ['genre_name']
        extra_kwargs = {"genre_name": {'required': True, 'allow_null': False}}


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "birthday", "sex"]


class AuthorShortInfo(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "middle_name"]


class AdditionalInfo(serializers.HyperlinkedModelSerializer):
    author = AuthorShortInfo(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ["title", "year", "num_of_pages", "price", "url", "images", "annotation", "book_id", "author"]
        extra_kwargs = {"title": {'required': True, 'allow_null': False},
                        "year": {'required': True, 'allow_null': False},
                        "images": {'required': True, 'allow_null': False}}

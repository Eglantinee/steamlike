from books.models import Book, Author, Genres, Publisher
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "price", "images", "book_id"]
        extra_kwargs = {"title": {'required': True, 'allow_null': False},
                        "price": {'required': True, 'allow_null': True},
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


class BookInfoSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorShortInfo(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ["title", "year", "num_of_pages", "price", "url", "images", "annotation", "book_id", "author",
                  'genres']
        extra_kwargs = {"title": {'required': True, 'allow_null': False},
                        "year": {'required': True, 'allow_null': False},
                        "images": {'required': True, 'allow_null': False}}


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'author_id')


class AuthorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

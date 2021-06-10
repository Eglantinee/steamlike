from rest_framework.decorators import action
from rest_framework.generics import ListAPIView

from books.models import Book, Genres
from books.serializers import BookSerializer, GenreSerializer, BookInfoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from books.pagination import StandardResultsSetPagination
from books.filters import MainFilter
from django_filters.rest_framework import DjangoFilterBackend


class BookViewSet(viewsets.ModelViewSet):
    """
    This class will be used to represent book full info and make some kind of sort
    """
    queryset = Book.objects.all()
    serializer_class = BookInfoSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        response = []
        if self.request.query_params.get('genre'):
            print(self.request.query_params.get('genre'))
            genres = self.request.query_params.get('genre').split(',')
            books = Book.objects.filter(genres__genre_name__in=genres)
            return books
        else:
            response = Book.objects.all()
        print(response)
        return response


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer


class BookInfoViewSet(viewsets.ModelViewSet):
    """Class to represent books with custom filtering"""
    serializer_class = BookInfoSerializer

    def get_queryset(self):
        response = Book.objects.all()
        return response


class BookSearchViewSet(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookInfoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['title', 'author__first_name', 'author__middle_name', 'author__last_name']
    filterset_fields = ['genre']
    ordering_fields = ['price']
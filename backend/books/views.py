from rest_framework.generics import ListAPIView

from books.models import Book, Genres, Author
from books.serializers import GenreSerializer, BookInfoSerializer, AuthorInfoSerializer, AuthorListSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from books.pagination import StandardResultsSetPagination
from books.filters import BookFilter
from django_filters.rest_framework import DjangoFilterBackend


class BookViewSet(viewsets.ModelViewSet):
    """
    This class will be used to represent book full info and make some kind of sort
    """
    queryset = Book.objects.all()
    serializer_class = BookInfoSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter


class GenresListView(ListAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer


class AuthorsListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer


class AuthorInfoView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorInfoSerializer

    def get_queryset(self):
        return Author.objects.filter(author_id=self.kwargs.get('pk'))

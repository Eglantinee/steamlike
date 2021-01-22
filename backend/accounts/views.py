from books.models import Book
from books.serializers import BookSerializer
from rest_framework import viewsets
from django.http import HttpResponse


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

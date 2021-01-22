from books.models import Book
from books.serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status


class BookViewSet(viewsets.ModelViewSet):
    # queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        print(type(Book.objects.all()))
        book = Book.objects.all()
        serializer = BookSerializer(data=book)
        return serializer.initial_data

    def create(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            print(serializer.data)
            # method for create data into DB
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

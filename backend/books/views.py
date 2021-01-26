from books.models import Book, Genres
from books.serializers import BookSerializer, GenreSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status


class BookViewSet(viewsets.ModelViewSet):
    # queryset = Book.objects.all()
    serializer_class = BookSerializer

    # permission_classes = [IsAdminUser]

    def get_queryset(self):
        params = self.request.query_params.dict()
        if params:
            print(params['filter'])
            response = Book.objects.filter(genres=1)
            serializer = BookSerializer(data=response)
            print(serializer.initial_data, '11111')
            return serializer.initial_data
        else:
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


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer

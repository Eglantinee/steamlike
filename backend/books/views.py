from rest_framework.decorators import action
from books.models import Book, Genres
from books.serializers import BookSerializer, GenreSerializer, AdditionalInfo
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status


class BookViewSet(viewsets.ModelViewSet):
    """
    This class will be used to represent books depends on chosen filters
    """
    serializer_class = BookSerializer

    def get_queryset(self):
        params = self.request.query_params.dict()
        for key, value in params.items():
            params[key] = value.split(',')

        response = None
        if params:
            for key in params.keys():
                for value in params[key]:
                    genre_id = Genres.objects.filter(genre_name=value).values('genre_id')
                    my_id = genre_id[0]['genre_id']
                    print(my_id)
                    response = Book.objects.filter(**{key: my_id})
        else:
            response = Book.objects.all()
        return response

    # can do this to provide some get requests for url /book/{id}/my_filter
    # @action(methods=['get'], detail=True)
    # def my_filter(self, request, pk):
    #     print(self.request)
    #     return Response(status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            # method for create data into DB
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer


class AdditionalBookInfo(viewsets.ModelViewSet):
    serializer_class = AdditionalInfo
    # queryset = Book.objects.all()

    def get_queryset(self):
        response = Book.objects.all()
        print(response)
        return response

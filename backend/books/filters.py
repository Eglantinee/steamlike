import django.core.exceptions
from django_filters import rest_framework as filters
from .models import Book
from django.db.models import Q


class GenreFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class BookFilter(filters.FilterSet):
    """
    Filtering
    """
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_date = filters.DateTimeFilter(field_name='year', lookup_expr='gte')
    max_date = filters.DateTimeFilter(field_name='year', lookup_expr='lte')
    genres = GenreFilter(field_name='genres__genre_name', lookup_expr='in')
    genre = GenreFilter(field_name='genres__genre_name', method='filter_genre')

    def filter_genre(self, queryset, name, value):
        if isinstance(value, list):
            for i in value:
                queryset = queryset.filter(genres__genre_name=i)
        return queryset

    """
    Searching
    """
    search = filters.CharFilter(method="search_filter")

    def search_filter(self, queryset, name, value):
        return queryset.filter(Q(author__first_name__icontains=value) |
                               Q(author__middle_name__icontains=value) |
                               Q(author__last_name__icontains=value) |
                               Q(title__icontains=value))

    order = filters.CharFilter(method='order_filter')

    def order_filter(self, queryset, name, value):
        # if value not in ["title", "year", "num_of_pages", "price", "book_id"]:
        #     return queryset
        try:
            return queryset.order_by(value)
        except django.core.exceptions.FieldError:
            return queryset

    class Meta:
        model = Book
        fields = ('price', 'year')

from rest_framework import filters


class MainFilter(filters.BaseFilterBackend):
    # if self.request.query_params.get('genre'):

    def filter_queryset(self, request, queryset, view):
        print(request)
        return queryset

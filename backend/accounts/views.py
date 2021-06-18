from functools import reduce
import operator
import django.utils.datastructures
from rest_framework.views import APIView
from rest_framework import permissions, generics
from rest_framework import filters as r_filters
from accounts.serializers import *
from rest_framework.response import Response
from django.contrib.auth.models import User
from accounts.models import Profile
from books.models import Book
from rest_framework import status
from django_filters import rest_framework as filters
from django.core.mail import send_mail
from django.core.exceptions import FieldError
from django.db.models import Q


class UserLogoutView(APIView):

    def get(self, request):
        try:
            request.user.auth_token.delete()
        except AttributeError:
            print("Anonymous User try to logout")
        return Response(status=status.HTTP_200_OK)


class CreateUserView(APIView):

    def post(self, request):
        post_data = request.data
        serializer = UserSerializer(data=post_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            send_mail(
                'Subject here',
                'Account was created.',
                'from@example.com',
                [serializer.data.get('email')],
                fail_silently=False,
            )
            print(serializer.data)
            return Response(data={'user': serializer.data})
        return Response(data={'user': serializer.errors})


class GetUserInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_info = UserInfoSerializer(Profile.objects.filter(user=request.user)[0])
        return Response(data=user_info.data)


class UpdateUserInfo(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user_info = Profile.objects.filter(user_id=request.user.id)[0]
        serializer = ProfileUpdateInfoSerializer(user_info, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            full_user = UserInfoSerializer(Profile.objects.filter(user=request.user)[0])
            return Response(data=full_user.data)
        return Response(data={'user': serializer.errors})


class StoreUserBook(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        post_data = request.data
        post_data.update({"user": request.user.id})

        account_balance = Profile.objects.filter(user=request.user)[0].balance
        book_price = Book.objects.filter(book_id=request.data['book'])[0].price
        if account_balance < book_price:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = UserStoredBooksSerializer(data=post_data)
        balance_serializer = ChangeUserBalanceSerializer(Profile.objects.filter(user=request.user)[0],
                                                         data={'balance': account_balance - book_price})
        if not balance_serializer.is_valid(raise_exception=True):
            return Response(data={'balance': serializer.errors})
        if not serializer.is_valid(raise_exception=True):
            return Response(data={'user': serializer.errors})

        balance_serializer.save()
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class UserCommentView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        post_data = request.data
        post_data.update({"user": request.user.id})
        if "comment_id" in post_data:
            comment = Comment.objects.filter(comment_id=post_data['comment_id'], user_id=request.user.id)
            try:
                comment = comment[0]
            except IndexError:
                print("Someone try to edit others comment")
                return Response(status=status.HTTP_400_BAD_REQUEST)
            serializer = CommentSerializer(comment, data=post_data)
        else:
            serializer = CommentSerializer(data=post_data)
        if not serializer.is_valid(raise_exception=True):
            return Response(data={'comment': serializer.errors})

        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        try:
            serializer = CommentSerializer(Comment.objects.filter(book_id=self.request.GET['id']), many=True)
            page = self.paginate_queryset(serializer.data)
            return self.get_paginated_response(page)
        except django.utils.datastructures.MultiValueDictKeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GenreFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    """
    Filtering
    """
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_date = filters.DateTimeFilter(field_name='date', lookup_expr='gte')
    max_date = filters.DateTimeFilter(field_name='date', lookup_expr='lte')
    genres = GenreFilter(field_name='book__genres__genre_name', lookup_expr='in')
    genre = GenreFilter(field_name='book_genres__genre_name', method='filter_genre')

    def filter_genre(self, queryset, name, value):
        lookup = '__'.join([name, ''])
        # print("enter")
        # print(queryset, name, value)
        if isinstance(value, list):
            for i in value:
                queryset = queryset.filter(book__genres__genre_name=i)
        return queryset
        #         conditions = reduce(operator.and_, [Q(book__genres__genre_name__in=v) for v in value])
        # print(conditions)
        # return queryset.filter(conditions)
        # return queryset.filter(book__genres__genre_name__in=value)
        # BookHasUser.objects.filter(book__title__icontains=)

    """
    Searching
    """
    search = filters.CharFilter(method="search_filter")

    def search_filter(self, queryset, name, value):
        # if len(value) < 3:
        #     return BookHasUser.objects.none()
        return queryset.filter(Q(book__author__first_name__icontains=value) |
                               Q(book__author__middle_name__icontains=value) |
                               Q(book__author__last_name__icontains=value) |
                               Q(book__title__icontains=value))

    order = filters.CharFilter(method='order_filter')

    def order_filter(self, queryset, name, value):
        try:
            return queryset.order_by(value)
        except FieldError:
            return queryset

    class Meta:
        model = BookHasUser
        fields = ('price', 'date',)


class UserLibraryView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = BookHasUser.objects.all()
    serializer_class = UserLibrarySerializer
    filterset_class = ProductFilter
    filter_backends = [filters.DjangoFilterBackend]

    def get_queryset(self):
        print(self.request.query_params)
        return BookHasUser.objects.filter(user_id=self.request.user.id)

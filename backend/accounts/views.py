
from rest_framework.views import APIView

from accounts.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User


class CreateUser(APIView):

    def post(self, request):
        post_data = request.data

        print(post_data)  # See what is your post DATA

        serializer = UserSerializer(data=post_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={'user': serializer.data})
        return Response(data={'user': serializer.errors})

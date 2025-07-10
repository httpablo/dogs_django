from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from . import serializers


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserCreateSerializer
    permission_classes = [AllowAny]

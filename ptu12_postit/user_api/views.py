from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from . import serializers


User = get_user_model()


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]

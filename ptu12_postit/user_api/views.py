from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from . import serializers


User = get_user_model()


class UserCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]

    def delete(self, request, *args, **kwargs):
        user = User.objects.filter(pk=request.user.pk)
        if user.exists():
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('You can only delete yourself.')

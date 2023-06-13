from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = models.Post
        fields = ['id', 'user', 'user_id', 'title', 'body', 'created_at']

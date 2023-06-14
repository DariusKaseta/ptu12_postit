from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    post = serializers.ReadOnlyField(source='post.id')
    like_count = serializers.SerializerMethodField()

    def get_like_count(self, obj):
        return models.CommentLike.objects.filter(comment=obj).count()

    class Meta:
        model = models.Comment
        fields = ['id', 'user', 'user_id', 'post', 'body', 'created_at', 'like_count']


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    comments = CommentSerializer(many=True, read_only=True)
    # comments = serializers.StringRelatedField(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()

    def get_comment_count(self, obj):
        return models.Comment.objects.filter(post=obj).count()
    
    def get_like_count(self, obj):
        return models.PostLike.objects.filter(post=obj).count()

    class Meta:
        model = models.Post
        fields = ['id', 'user', 'user_id', 'title', 'body', 'created_at', 
                  'like_count', 'comment_count', 'comments']


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PostLike
        fields = ['id']


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentLike
        fields = ['id']

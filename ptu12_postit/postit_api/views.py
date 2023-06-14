from django.utils.translation import gettext_lazy as _
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from . import models, serializers


class PostList(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        post = models.Post.objects.filter(
            pk=kwargs['pk'], 
            user=request.user
        )
        if post.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError(_('You have no rights to update this.'))

    def delete(self, request, *args, **kwargs):
        post = models.Post.objects.filter(
            pk=kwargs['pk'], 
            user=request.user
        )
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError(_('You have no rights to delete this.'))


class CommentList(generics.ListCreateAPIView):
    # queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        post = models.Post.objects.get(pk=self.kwargs['post_pk'])
        serializer.save(user=self.request.user, post=post)

    def get_queryset(self):
        post = models.Post.objects.get(pk=self.kwargs['post_pk'])
        return models.Comment.objects.filter(post=post)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def put(self, request, *args, **kwargs):
        try:
            comment = models.Comment.objects.get(pk=kwargs['pk'], user=request.user)
        except Exception as e:
            raise ValidationError(_('You cannot update this.'))
        else:
            return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        try:
            comment = models.Comment.objects.get(pk=kwargs['pk'], user=request.user)
        except Exception as e:
            raise ValidationError(_('You cannot delete this.'))
        else:
            return self.destroy(request, *args, **kwargs)

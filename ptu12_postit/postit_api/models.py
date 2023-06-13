from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Post(models.Model):
    title = models.CharField(_("title"), max_length=250)
    body = models.TextField(_("body"), max_length=10000)
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name='posts',
    )
    created_at = models.DateTimeField(
        _("created at"), 
        auto_now_add=True, 
        db_index=True,
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def __str__(self):
        return f"{self.title} {_('posted by')} {self.user}"

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, 
        verbose_name=_("post"), 
        on_delete=models.CASCADE,
        related_name='comments',
    )
    body = models.TextField(_("body"), max_length=10000)
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name='comments',
    )
    created_at = models.DateTimeField(
        _("created at"), 
        auto_now_add=True, 
        db_index=True,
    )

    class Meta:
        ordering = ['created_at']
        verbose_name = _("comment")
        verbose_name_plural = _("comments")

    def __str__(self):
        return f"{self.post} {_('commented by')} {self.user}"

    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={"pk": self.pk})


class PostLike(models.Model):
    post = models.ForeignKey(
        Post, 
        verbose_name=_("post"), 
        on_delete=models.CASCADE,
        related_name='likes',
    )
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name='post_likes',
    )

    class Meta:
        verbose_name = _("post like")
        verbose_name_plural = _("post likes")

    def __str__(self):
        return f"{self.post.title} {_('liked by')} {self.user}"

    def get_absolute_url(self):
        return reverse("postlike_detail", kwargs={"pk": self.pk})


class CommentLike(models.Model):
    comment = models.ForeignKey(
        Comment, 
        verbose_name=_("comment"), 
        on_delete=models.CASCADE,
        related_name='likes',
    )
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name='comment_likes',
    )

    class Meta:
        verbose_name = _("comment like")
        verbose_name_plural = _("comment likes")

    def __str__(self):
        return f"{self.comment} {_('liked by')} {self.user}"

    def get_absolute_url(self):
        return reverse("commentlike_detail", kwargs={"pk": self.pk})

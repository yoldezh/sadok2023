from django.db import models
from django.contrib.auth import get_user_model

class CreationModificationMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)
        indexes = [
            models.Index(fields=['-created_at']),
        ]


class Post(CreationModificationMixin):
    content = models.CharField(max_length=500, blank=True,  default='')
    image = models.ImageField(upload_to='images/posts', default='images/default.jpg')  # Spécifiez une valeur par défaut appropriée
    class Meta(CreationModificationMixin.Meta):
        pass

class Media(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='media')
    image = models.ImageField(upload_to='images/posts')
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(CreationModificationMixin):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=500)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comment_likes')  # Change related_name
    users_like = models.ManyToManyField(get_user_model(), related_name='liked_comments')

    class Meta:
        ordering = ('-created_at',)
        indexes = [
            models.Index(fields=['-created_at']),
        ]

class LikedComments(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comment_likers')  # Change related_name
    created_at = models.DateTimeField(auto_now_add=True)

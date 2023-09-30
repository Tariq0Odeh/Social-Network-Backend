from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f" {self.title} ({self.id}) - {self.user.name}"


class Comment(models.Model):
    body = models.TextField(blank=False)
    user = models.ForeignKey(User, related_name='comments',
                             on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments',
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.body} ({self.id}) - {self.post.title}"


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes',
                             on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='likes',
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.post.title}"

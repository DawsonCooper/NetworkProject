from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=24, default="None")
    bio = models.TextField(default="")
    profilePicture = models.ImageField(
        upload_to="network/static/images", default=False, blank=True, null=True)


class Post(models.Model):
    userId = models.IntegerField(User, default=None)
    caption = models.TextField(default="")
    image = models.ImageField(
        upload_to="network/static/images", default=False, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    totalLikes = models.IntegerField(default=0)
    totalComments = models.IntegerField(default=0)


class Likes(models.Model):
    userId = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    postId = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)


class Comment(models.Model):
    userId = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    postId = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)

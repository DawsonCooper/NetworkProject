from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=24)
    bio = models.CharField(max_length=150)


class Post(models.Model):
    userId = models.ForeignKey(User, default=None)
    caption = models.CharField(max_length=300)
    image = models.ImageField(default=None)
    timestamp = models.DateTimeField(auto_now_add=True)
    totalLikes = models.IntegerField(default=0)
    totalComments = models.IntegerField(default=0)


class Likes(models.Model):
    userId = models.ForeignKey(User, default=None)
    postId = models.ForeignKey(Post, default=None)


class Comment(models.Model):
    userId = models.ForeignKey(User, default=None)
    postId = models.ForeignKey(Post, default=None)
    content = models.CharField(max_length=150)

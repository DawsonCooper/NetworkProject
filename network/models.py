from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=24, default="None")
    bio = models.TextField(default="")
    profilePicture = models.ImageField(
        upload_to="network/static/images/", default=False, blank=True, null=True)


class Post(models.Model):
    username = models.CharField(
        default='None', max_length=24, null=True, blank=True)
    caption = models.TextField(default="")
    image = models.ImageField(
        upload_to="network/static/images/", default=False, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    totalLikes = models.IntegerField(default=0)
    totalComments = models.IntegerField(default=0)

    def get_user(self):
        refrence = User.objects.filter(username=self.username).values()
        return {'refrence': refrence}

    def total_interactions(self):
        return {'interactions': self.totalLikes + self.totalComments}

    def serailize(self):
        return {
            'username': self.username,
            'caption': self.caption,
            'image': self.image,
            'timestamp': self.timestamp,
            'totalLikes': self.totalLikes,
            'totalComments': self.totalComments
        }


class Likes(models.Model):
    username = models.CharField(default=None, max_length=24)
    post = models.IntegerField(default=None)
    status = models.BooleanField(default=None)

    def get_user(self):
        refrence = User.objects.filter(username=self.username).values()
        return {'refrence': refrence}

    def serialize(self):
        return {'username': self.username, 'post': self.post}


class Comment(models.Model):
    username = models.CharField(default=None, max_length=24)
    post = models.IntegerField(default=None)
    content = models.CharField(max_length=150)

    def serialize(self):
        return {
            "username": self.username,
            'post': self.post,
            'content': self.content,
        }

    def get_user(self):
        refrence = User.objects.filter(username=self.username).values()
        return {'refrence': refrence}

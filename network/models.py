from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=24, default="Incognito")
    bio = models.TextField(default="")
    profilePicture = models.ImageField(
        upload_to="network/static/images/", default=False, blank=True, null=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)


class Realationships(models.Model):
    followerId = models.IntegerField()
    followingId = models.IntegerField()


class Post(models.Model):
    username = models.CharField(
        default='None', max_length=24, null=True, blank=True)
    caption = models.TextField(default="")
    timestamp = models.DateTimeField(auto_now_add=True)
    totalLikes = models.IntegerField(default=0)
    totalComments = models.IntegerField(default=0)

    def serialize(self):
        return {
            'id': self.pk,
            'username': self.username,
            'caption': self.caption,
            'timestamp': self.timestamp,
            'totalLikes': self.totalLikes,
            'totalComments': self.totalComments
        }

    def get_user(self):
        refrence = User.objects.filter(username=self.username).values()
        return {'refrence': refrence}

    def total_interactions(self):
        return {'interactions': self.totalLikes + self.totalComments}


class Likes(models.Model):
    """ STATUS TRACKS THE USERS INTERACTION WITH LIKE/DISLIKE BUTTON USING -1, 0, 1 """
    username = models.CharField(default=None, max_length=24)
    post = models.IntegerField(default=None)
    status = models.IntegerField(default=0)

    def get_user(self):
        refrence = User.objects.filter(username=self.username).values()
        return {'refrence': refrence}

    def serialize(self):
        return {'username': self.username, 'post': self.post, 'status': self.status}


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

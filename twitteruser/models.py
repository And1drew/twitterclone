from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class tweeter(AbstractUser):
    displayname = models.CharField(max_length=50, default='')
    password = models.CharField(default='', max_length=50)
    following = models.ManyToManyField("self", symmetrical=False)


class tweet(models.Model):
    author = models.ForeignKey(tweeter, on_delete=models.CASCADE)
    description = models.TextField(default='', max_length=140)
    date = models.DateTimeField(default=timezone.now)
    # likes = models.IntegerField(default=0)
    # dislikes = models.IntegerField(default=0)
    # vote_score = models.IntegerField(default=0)


class notifications(models.Model):
    """
    who is it for?
    what tweet was it made from?
    has it been seen?
    """
    pass

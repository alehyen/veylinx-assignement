from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Hashtag(models.Model):
    id_hashtag = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)


class Post(models.Model):
    """
        Note: I'm using the built in User model to reference the user in the post,
        otherwise if we need other custom fields we can create a custom User class and
        use a OneToOneField relation with the built-in User model
    """
    id_post = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    # for the soft delete
    deleted = models.BooleanField(default=False)
    tags = models.ManyToManyField(Hashtag)

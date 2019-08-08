from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class TweetPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=240)
    is_deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post

class Friends(models.Model):
    follows = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='Owner', null=True, on_delete=models.CASCADE)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.follows.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, old_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.follows.remove(old_friend)
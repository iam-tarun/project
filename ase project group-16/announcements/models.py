from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    groupid = models.IntegerField(null=True)
    title = models.CharField(max_length=50, unique=False)
    desc = models.TextField(max_length=200, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name.username} Post'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


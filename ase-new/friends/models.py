from django.db import models
from django.contrib.auth.models import User

class Friends(models.Model):
    user1 = models.TextField(max_length=30, null=True)
    user2 = models.TextField(max_length=30, null=True)

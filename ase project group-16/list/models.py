from django.db import models
from django.contrib.auth.models import User


class Itemlist(models.Model):
    name = models.ForeignKey(User, default=None)
    item = models.TextField(max_length=50)
from django.db import models
from django.contrib.auth.models import User

class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()

class Leaderboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    borrowed_n = models.IntegerField(default=0)
    shared_n = models.IntegerField(default=0)
    total_rating = models.IntegerField(default=0)
    avg_rating = models.FloatField(default=3)
    points = models.FloatField(default=0)

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.TextField()

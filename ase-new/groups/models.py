from django.db import models
from django.contrib.auth.models import User


class GroupTable(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    desc = models.TextField(max_length=50, blank=True)
    image = models.ImageField(default='group_pics/default.jpg', upload_to='group_pics')
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} GroupTable'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class GroupUserTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupTable, on_delete=models.CASCADE)
    status = models.IntegerField(max_length=1, null=True)

    def __str__(self):
        return f'{self.user.username} GroupUserTable'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Invitation(models.Model):
    groupid = models.IntegerField()
    notifId = models.IntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

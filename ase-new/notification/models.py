from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Notification(models.Model):
    item_name = models.CharField(max_length=256,null=True)
    title = models.CharField(max_length=256,null=True)
    return_date = models.DateField(null=True)
    return_time = models.TimeField(null=True)
    message = models.TextField()
    viewed = models.BooleanField(default=False)
    curr_user = models.TextField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    types = [('PERSONAL', 'Personal'), ('ITEM', 'Item'), ('GROUP', 'Group'), ('FRIEND','Friend')]
    type = models.CharField(max_length=8, choices=types, default="PERSONAL")


@receiver(post_save, sender=User)
def create_welcome_message(sender, **kwargs):
    if kwargs.get('created', False):
        Notification.objects.create(user=kwargs.get('instance'),
                                    title="Welcome to our ShareZone site!",
                                    message="Thanks for signing up!",
                                    curr_user="ShareZone")

class SharedItemsList(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=256)
    shared_user = models.TextField(max_length=30)
    borrowed_user = models.TextField(max_length=30)

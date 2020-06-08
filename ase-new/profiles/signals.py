from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profiles, Backgroundimage
from rating.models import Leaderboard

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profiles.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profiles.save()

@receiver(post_save, sender=User)
def create_backgroundimage(sender, instance, created, **kwargs):
    if created:
        Backgroundimage.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_backgroundimage(sender, instance, **kwargs):
    instance.backgroundimage.save()


@receiver(post_save, sender=User)
def create_leaderboard(sender, instance, created, **kwargs):
    if created:
        Leaderboard.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_leaderboard(sender, instance, **kwargs):
    instance.leaderboard.save()

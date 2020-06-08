from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    phone = PhoneNumberField(null=True, blank=False, unique=True)

    def __str__(self):
        return f'{self.user.username} Profiles'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Backgroundimage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bg = models.ImageField(default='background/default.jpg', upload_to='background')

    def __str__(self):
        return f'{self.user.username} Backgroundimage'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

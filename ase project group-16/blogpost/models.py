from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from groups.models import GroupTable


# Create your models here.
class Comments(models.Model):
    objid = models.IntegerField(default=0)
    content = models.TextField()
    author = models.CharField(max_length=20)
    date_posted = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        super(Comments, self).save()


class Bpost(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='photos/default.jpg', upload_to='photos')
    likes = models.IntegerField(default=0)
    likelist = models.CharField(default='', max_length=1000)
    group = models.ForeignKey(GroupTable, on_delete=models.CASCADE, null=True)

    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        super(Bpost, self).save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

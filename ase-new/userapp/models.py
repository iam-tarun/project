from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Itemlist(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=50)
    conditions = [('GD', 'Good'), ('AVG', 'Average'), ('BD', 'Bad')]
    condition = models.CharField(max_length=3, choices=conditions, default='AVG')
    categories = [('ELEC', 'Electronics'), ('STAT', 'Stationary'), ('CLOTH', 'Clothes'), ('FTW', 'Footwear'),
                  ('BAGS', 'Bags'), ('OTHER', 'Other')]
    Category = models.CharField(max_length=5, choices=categories, default='OTHER')
    date_created = models.DateTimeField(default=timezone.now)

    status = [('AVAILABLE', 'Available'), ('NOT-AVAILABLE','Not-Available')]
    ItemStatus = models.CharField(max_length=13, choices=status, default="AVAILABLE")
    Image = models.ImageField(default='Items_pics/default.jpg', upload_to='Items_pics')

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse('dashboard')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

from django.db import models
from django.utils import timezone
import datetime

class Menu(models.Model):
    item = models.CharField(max_length=50)
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    image = models.ImageField()
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.item

class UserObjects(models.Model):
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    like_status = models.BooleanField(default=False)
    date_liked = models.DateField(default= timezone.now)


"""
    def was_voted_recently(self):
        if self.last_voted <=  timezone.now() - datetime.timedelta(hours=5, minutes=59, seconds=59):
            self.votes =0

        #return self.votes
"""
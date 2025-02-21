from django.db import models
from django.contrib.auth.models import User

class bill_Data(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    room = models.CharField(max_length=100)
    rent = models.IntegerField(default=0)
    electricity = models.IntegerField(default=0)
    water = models.IntegerField(default=0)
    food = models.IntegerField(default=0)
    parking = models.IntegerField(default=0)

    def __str__(self):
        return self.room
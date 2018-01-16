from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Training(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    date_taken = models.DateField(default=datetime.now)
    account = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title


class TimeOff(models.Model):
    date_taken = models.DateField(default=datetime.now)
    hours = models.IntegerField(default=8)
    account = models.CharField(max_length=50)

    def __str__(self):
        return '%s:%s' % (self.account, self.hours)


class Outage(models.Model):
    title = models.CharField(max_length=50)
    date_occured = models.DateTimeField(default=datetime.now)
    description = models.TextField(blank=True, null=True)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

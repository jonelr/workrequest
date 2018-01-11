from datetime import datetime

from django.db import models


# Create your models here.
class Training(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    date_taken = models.DateField(default=datetime.now)
    account = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

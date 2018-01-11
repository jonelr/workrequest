from django.db import models
from datetime import datetime

# Create your models here.
class Training(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    date_taken = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title
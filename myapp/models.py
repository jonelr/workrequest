from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


# Create your models here.

class Area(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Plant(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Status(models.Model):
    class Meta:
        verbose_name_plural = "Statuses"

    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class BusinessUnit(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class WorkRequest(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Hours(models.Model):
    class Meta:
        verbose_name_plural = "Hours"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    workrequest = models.ForeignKey(WorkRequest, on_delete=models.CASCADE)
    week_ending = models.DateField(default=datetime.now)
    hours = models.IntegerField(default=8)



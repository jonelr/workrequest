from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


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

    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    account = models.CharField(max_length=50, blank=True, null=True)
    workrequest = models.ForeignKey(WorkRequest, on_delete=models.CASCADE)
    week_ending = models.DateField(default=datetime.now)
    hours = models.IntegerField(default=8)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'Record %s' % self.id


class TimeSheet(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    week_ending = models.DateField(default=datetime.now)
    hours = models.IntegerField()

    def __str__(self):
        return '%s - %s:%d' % (self.week_ending, self.account, self.hours)


class SqlVersion(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class OsVersion(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Landscape(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


def get_default_landscape():
    """Returns default Landscape foreign key value of Production"""
    return Landscape.objects.get(id=4).id


class SqlServer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    cpu = models.IntegerField(default=4)
    ram = models.IntegerField()
    date_added = models.DateField(auto_now=True)
    version = models.ForeignKey(
        SqlVersion, on_delete=models.CASCADE, related_name='servers')
    os = models.ForeignKey(
        OsVersion, on_delete=models.CASCADE, related_name='servers')
    sap = models.BooleanField(default=False)
    mes = models.BooleanField(default=False)
    monitor = models.BooleanField(default=True)
    port = models.IntegerField(default=1433)
    landscape = models.ForeignKey(
        Landscape, on_delete=models.CASCADE, default=4)
    online = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '%s:%s' % (self.id, self.name)


class SqlLog(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(default=datetime.now)
    time_added = models.TimeField(default=datetime.now())
    description = models.TextField(blank=True, null=True)
    # servers = models.ForeignKey(SqlServer, on_delete=models.CASCADE, related_name='logs')
    servers = models.ManyToManyField(SqlServer)
    account = models.CharField(max_length=50, )

    def __str__(self):
        return self.title

    def __repr__(self):
        return '%s:%s' % (self.id, self.title)


class WebApplication(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date_added = models.DateField(auto_now=True)
    url = models.CharField(max_length=100)
    online = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '%s:%s' % (self.id, self.name)

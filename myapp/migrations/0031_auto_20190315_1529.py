# Generated by Django 2.1.7 on 2019-03-15 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_auto_20190315_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='webapplication',
            name='online',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='sqllog',
            name='time_added',
            field=models.TimeField(default=datetime.datetime(2019, 3, 15, 15, 29, 57, 160848)),
        ),
    ]
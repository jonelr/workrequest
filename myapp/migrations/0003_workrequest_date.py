# Generated by Django 2.0.1 on 2018-01-09 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180109_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='workrequest',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

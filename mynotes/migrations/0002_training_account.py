# Generated by Django 2.0.1 on 2018-01-11 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='account',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
# Generated by Django 2.0.1 on 2018-01-11 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_hours_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='sqlserver',
            name='sap',
            field=models.BooleanField(default=False),
        ),
    ]

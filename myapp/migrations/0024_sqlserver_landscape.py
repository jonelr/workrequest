# Generated by Django 2.0.1 on 2018-01-18 12:46

from django.db import migrations, models
import django.db.models.deletion
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_auto_20180117_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='sqlserver',
            name='landscape',
            field=models.ForeignKey(default=myapp.models.get_default_landscape, on_delete=django.db.models.deletion.CASCADE, to='myapp.Landscape'),
        ),
    ]

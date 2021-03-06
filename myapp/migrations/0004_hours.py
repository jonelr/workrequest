# Generated by Django 2.0.1 on 2018-01-09 22:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0003_workrequest_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_ending', models.DateField(default=datetime.datetime.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workrequest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.WorkRequest')),
            ],
        ),
    ]

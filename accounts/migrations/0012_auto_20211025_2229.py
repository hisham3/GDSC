# Generated by Django 3.2.8 on 2021-10-25 20:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0011_alter_projects_finish_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='members',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projects',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 22, 29, 3, 199692)),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-25 21:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_projects_finish_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 23, 21, 29, 262732)),
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-19 05:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_doclogin_time_alter_docreg_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doclogin',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 19, 11, 28, 37, 364934)),
        ),
        migrations.AlterField(
            model_name='docreg',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 19, 11, 28, 37, 364934)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Message',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 19, 11, 28, 37, 364934)),
        ),
        migrations.AlterField(
            model_name='nurselogin',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 19, 11, 28, 37, 364934)),
        ),
        migrations.AlterField(
            model_name='nursereg',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 19, 11, 28, 37, 364934)),
        ),
    ]

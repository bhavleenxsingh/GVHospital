# Generated by Django 5.0.6 on 2024-06-18 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_feedback_patientinfo_department_patientinfo_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nursereg',
            name='ConfirmPassword',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='doclogin',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 18, 17, 15, 51, 959341)),
        ),
        migrations.AlterField(
            model_name='docreg',
            name='Confirm_Password',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='docreg',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 18, 17, 15, 51, 959341)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 18, 17, 15, 51, 959341)),
        ),
        migrations.AlterField(
            model_name='nurselogin',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 18, 17, 15, 51, 959341)),
        ),
        migrations.AlterField(
            model_name='nursereg',
            name='Password',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='nursereg',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 18, 17, 15, 51, 959341)),
        ),
    ]

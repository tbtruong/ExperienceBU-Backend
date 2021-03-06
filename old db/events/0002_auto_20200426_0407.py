# Generated by Django 3.0.4 on 2020-04-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.TextField(default='CAS', max_length=40),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TextField(default='12:00:00', max_length=60),
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.TextField(default='GENERAL_MEETING', max_length=20),
        ),
    ]

# Generated by Django 3.0.4 on 2020-04-18 20:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='clubMeetingTime',
            field=models.TimeField(default=datetime.datetime(2020, 4, 18, 20, 22, 18, 225774, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='club',
            name='clubPicture',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
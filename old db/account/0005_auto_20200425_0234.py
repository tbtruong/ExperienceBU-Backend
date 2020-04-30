# Generated by Django 3.0.4 on 2020-04-25 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_event_date'),
        ('organizations', '0007_auto_20200422_1628'),
        ('userAccount', '0004_delete_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='events',
            field=models.ManyToManyField(to='events.Event'),
        ),
        migrations.AddField(
            model_name='profile',
            name='schedule',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='subscriptions',
            field=models.ManyToManyField(to='organizations.Club'),
        ),
        migrations.AddField(
            model_name='profile',
            name='tags',
            field=models.TextField(default='No Tags'),
        ),
    ]

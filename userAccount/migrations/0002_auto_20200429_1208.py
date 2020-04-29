# Generated by Django 3.0.4 on 2020-04-29 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20200427_2216'),
        ('organizations', '0009_auto_20200427_1638'),
        ('userAccount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='favoriteEvents', to='events.Event'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='subscriptions',
            field=models.ManyToManyField(blank=True, related_name='subscribedClubs', to='organizations.Club'),
        ),
    ]

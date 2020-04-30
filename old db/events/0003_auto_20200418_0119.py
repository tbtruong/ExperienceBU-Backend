# Generated by Django 3.0.4 on 2020-04-18 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200415_2230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='author',
            new_name='eventAffiliation',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='location',
            new_name='eventLocation',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='title',
            new_name='eventName',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='tags',
            new_name='eventTags',
        ),
        migrations.RemoveField(
            model_name='event',
            name='date_posted',
        ),
    ]

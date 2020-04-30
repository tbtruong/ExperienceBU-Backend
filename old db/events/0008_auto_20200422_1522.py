# Generated by Django 3.0.4 on 2020-04-22 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20200422_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='eventAffiliation',
            new_name='affiliation',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='contact_info',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventLocation',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='banner',
            new_name='picture',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventTags',
            new_name='tags',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventTime',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventType',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='event',
            name='eventID',
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]

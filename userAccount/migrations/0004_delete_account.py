# Generated by Django 3.0.4 on 2020-04-18 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20200418_0120'),
        ('userAccount', '0003_profile_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]

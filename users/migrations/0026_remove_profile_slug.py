# Generated by Django 2.2.4 on 2020-11-04 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_profile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
    ]

# Generated by Django 2.2.4 on 2020-10-31 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20201031_0445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
    ]

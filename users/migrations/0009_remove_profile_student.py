# Generated by Django 2.2.4 on 2020-10-17 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20201017_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='student',
        ),
    ]
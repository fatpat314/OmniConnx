# Generated by Django 3.1.3 on 2020-11-11 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_messages_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='status',
        ),
    ]

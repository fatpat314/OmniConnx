# Generated by Django 3.1.3 on 2020-11-11 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='status',
            field=models.CharField(choices=[('send', 'send'), ('accepted', 'accepted')], default=None, max_length=8),
        ),
    ]

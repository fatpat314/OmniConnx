# Generated by Django 3.0.7 on 2020-12-02 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(default='default.jpg', upload_to='media/profile_pics')),
                ('_id', models.IntegerField(blank=True, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='categorys.Node')),
            ],
            options={
                'verbose_name_plural': 'Nodes',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of your page.', max_length=600, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.CharField(blank=True, editable=False, help_text='Unique URL path to access this page. Generated by the system.', max_length=600, null=True)),
                ('content', models.TextField(help_text='Write the content of your page here.')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The date and time this page was created. Automatically generated when the model saves.', null=True)),
                ('modified', models.DateTimeField(auto_now=True, help_text='The date and time this page was updated. Automatically generated when the model updates.', null=True)),
                ('author', models.ForeignKey(help_text='The user that posted this article.', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='categorys.Listing')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Categories',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('categorys.node',),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Sub Categories',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('categorys.node',),
        ),
        migrations.AddField(
            model_name='listing',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorys.SubCategory'),
        ),
    ]

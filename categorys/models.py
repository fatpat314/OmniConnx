import datetime

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Categorys(models.Model):
    categorys_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.categorys_text

    def was_published_recently(self):
        return self.pub_date >= timezome.now() - datetime.timedelta(days=1)

class Subcategorys(models.Model):
    subcategory_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('pubdate')

    def __str__(self):
        return self.subcategory_text

    def was_published_recently(self):
        return self.pub_date >= timezome.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    categorys = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

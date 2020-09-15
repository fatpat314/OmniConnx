import datetime

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from .managers import CategoryManager, SubCategoryManager

# Create your models here.
class Node(models.Model):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Nodes'

class Category(Node):
    objects = CategoryManager()
    class Meta:
        proxy = True
        verbose_name_plural = 'Categories'

class SubCategory(Node):
    objects = SubCategoryManager()
    class Meta:
        proxy = True
        verbose_name_plural = 'Sub Categories'

class Listing(models.Model):
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

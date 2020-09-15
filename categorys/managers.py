from django.db import models

class CategoryManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(parent=None)

class SubCategoryManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().exclude(parent=None)

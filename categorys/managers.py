from django.db import models

class CategoryManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(parent=None)

class SubCategoryManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().exclude(parent=None)

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/my-new-wiki-page). """
        path_components = {'pk': self.pk}
        return reverse('index_all')

from django.db import models

class CategoryManager(models.Manager):
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)
    def get_queryset(self):
        return super().get_queryset().filter(parent=None)

class SubCategoryManager(models.Manager):

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=False
    )

    def get_queryset(self):
        return super().get_queryset().exclude(parent_id=None)

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/my-new-wiki-page). """
        path_components = {'pk': self.pk}
        return reverse('index_all')

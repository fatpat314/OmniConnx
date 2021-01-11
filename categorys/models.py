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
    image = models.ImageField(default='default.jpg', upload_to='media/profile_pics')
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True
    )
    _id = models.IntegerField(null=True, blank=True)
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)



    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Nodes'

class Category(Node):
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)
    # test = models.TextField(blank=True, null=True)
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
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=False)
    # name = models.CharField(max_length=100)
    """ Represents a single wiki page. """
    title = models.CharField(max_length=settings.WIKI_PAGE_TITLE_MAX_LENGTH, unique=True, null=True, help_text="Title of your page.")
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=False, help_text="The user that posted this article.")
    slug = models.CharField(max_length=settings.WIKI_PAGE_TITLE_MAX_LENGTH, blank=True, editable=False, null=True, help_text="Unique URL path to access this page. Generated by the system.")
    content = models.TextField(help_text="Write the content of your page here.")
    created = models.DateTimeField(auto_now_add=True, null=True, help_text="The date and time this page was created. Automatically generated when the model saves.")
    modified = models.DateTimeField(auto_now=True, null=True, help_text="The date and time this page was updated. Automatically generated when the model updates.")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/my-new-wiki-page). """
        path_components = {'pk': self.pk}
        return reverse('post', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Listing, self).save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

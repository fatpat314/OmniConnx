import uuid
import random
import string

from django.utils.text import slugify

def get_random_code():
    code = str(uuid.uuid4())[:8].replace('-', '').lower()
    return code

def random_string_generator(instance, new_slug=None):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_Slug
    else:
        slug = slugify(instance.user)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

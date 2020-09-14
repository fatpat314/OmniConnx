from django.contrib import admin

# Register your models here.
from .models import Categorys, Subcategorys
admin.site.register(Categorys)
admin.site.register(Subcategorys)

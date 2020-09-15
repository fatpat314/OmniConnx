from django.contrib import admin

# Register your models here.
from .models import Category, SubCategory, Listing

class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 3
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_editable = ('parent',)
    feildsets = (
        (
            None,{
                'fields': ('name',)
            }
        ),
    )
    inlines = (SubCategoryInline,)

admin.site.register(Category, CategoryAdmin)


class ListingInline(admin.TabularInline):
    model = Listing
    extra = 3


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('parent', 'name', 'listing_count')
    fieldsets = (
        (
            None, {
                'fields': ('name',)
            }
        ),
    )
    inlines = (ListingInline,)

    def listing_count(self, obj):
        return obj.listing_set.count()

    def get_ordering(self, request):
        return('parent', 'name')

admin.site.register(SubCategory, SubCategoryAdmin)

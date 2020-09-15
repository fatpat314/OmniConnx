from django.shortcuts import render
from .models import Category, SubCategory, Listing


def index_view(request, parent_or_child=None, pk=None):
    categories = Category.objects.filter(parent=None)

    if parent_or_child is None:
        listings = Listing.objects.all()

    elif parent_or_child == 'child':
        sub_cat = SubCategory.objects.get(pk=pk)
        listings = sub_cat.listing_set.all()

    elif parent_or_child == 'parent':
        listings = []
        sub_cats = Category.objects.get(pk=pk).children.all()

        for sub_cat in sub_cats:
            prds = sub_cat.listing_set.all()
            listings += prds
    else:
        listings = []

    return render(
        request,
        'categorys/index.html',
        {'categories': categories, 'listings': listings}
    )

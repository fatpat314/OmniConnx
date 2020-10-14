from django.shortcuts import render
from .models import Category, SubCategory, Listing
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Listing
from .forms import PageForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.template import loader

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



def home_view(request):
    return render(request, "home.html")

def about_view(request):
    return render(request, "about.html")

def student_view(request, parent_or_child=None, pk=None):
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
        'for_students.html',
        {'categories': categories, 'listings': listings}
    )
    # return render(request, "for_students.html")

def professionals_view(request, parent_or_child=None, pk=None):
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
        'for_professionals.html',
        {'categories': categories, 'listings': listings}
    )
    # return render(request, "for_professionals.html")


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

def listing_view(request, parent_or_child=None, pk=None):

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
        'categorys/listings.html',
        {'categories': categories, 'listings': listings}
    )


# class PageListView(ListView):
#     """ Renders a list of all Pages. """
#     model = Listing
#
#     def get(self, request):
#         """ GET a list of Pages. """
#         listings = self.get_queryset().all()
#         return render(request, 'post.html', {
#           'categories': categories, 'listings': listings
#         })
#
class PageDetailView(DetailView):
    """ Renders a specific page based on it's pk."""
    model = Listing

    def get(self, request, pk=None): #slug
        """ Returns a specific wiki page by pk. """
        post = self.get_queryset().get(pk=pk)
        return render(request, 'categorys/post.html', {
          'post': post
        })

# class PageListView(ListView):
#     """ Renders a list of all Pages. """
#     model = Listing
#
#     def get(self, request, parent_or_child=None, pk=None):
#         """ GET a list of Pages. """
#         categories = Category.objects.filter(parent=None)
#
#         if parent_or_child is None:
#             listings = Listing.objects.all()
#
#         elif parent_or_child == 'child':
#             sub_cat = SubCategory.objects.get(pk=pk)
#             listings = sub_cat.listing_set.all()
#
#         elif parent_or_child == 'parent':
#             listings = []
#             sub_cats = Category.objects.get(pk=pk).children.all()
#
#             for sub_cat in sub_cats:
#                 prds = sub_cat.listing_set.all()
#                 listings += prds
#         else:
#             listings = []
#
#         return render(
#             request,
#             'users/profile.html',
#             {'categories': categories, 'listings': listings}
#         )

class New_wiki_form(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': PageForm()}
        return render(request, 'categorys/new-wiki-form.html', context)

    def post(self, request, *args, **kwargs):
        form = PageForm(request.POST)
        if form.is_valid():
            new_wiki_form = form.save()
            return HttpResponseRedirect(reverse_lazy('post', args=[new_wiki_form.id]))
        return render(request, 'categorys/new-wiki-form.html', {'form':form})

@method_decorator([login_required], name='dispatch')
class Post_edit_view(UpdateView):
    model = Listing
    fields = ['title', 'content']
    template_name = 'categorys/post_edit.html'
    success_url = reverse_lazy('index_all')

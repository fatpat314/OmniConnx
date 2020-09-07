from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView

from listings.models import Listings

# Create your views here.
class CategoryListView(ListView):
    """Render a list of all Categorys"""
    model = Listings
    def get(self, request):
        """GET list of categorys"""
        listings = self.get_queryset().all()
        return render(request, 'listings/index.html',{
        'listings': listings,
        })

# def index(request):
#     latest_listing_list = Listings.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('listings/index.html')
#     context = {
#         'latest_listing list': latest_listing_list,
#     }
#     return HttpResponse(template.render(context, request))

# def detail(request, listing_id):
#     try:
#         listing = Listings.objects.get(pk=listing_id)
#     except Listings.doesNotExsist:
#         raise Http404("Listing does not exist")
#     return render(request, 'listings/detail.html', {'listing': listing})
#
# def result(request, listing_id):
#     response ="You are looking at the results of Listing %s." % listing_id
#     return HttpResponse("You're voteing on Listing %s." % listing_id)

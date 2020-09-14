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

from categorys.models import Categorys, Subcategorys

# Create your views here.
class CategorysListView(ListView):
    """Render a list of all Categorys"""
    model = Categorys
    def get(self, request):
        """GET list of categorys"""
        categorys = self.get_queryset().all()
        return render(request, 'categorys/index.html',{
        'categorys': categorys,
        })

class SubcategorysListView(ListView):
    model = Subcategorys
    def get(self, request):
        """GET list of categorys"""
        subcategorys = self.get_queryset().all()
        return render(request, 'categorys/subcategorys.html',{
        'subcategorys': subcategorys,
        })

class CategorysDetailView(DetailView):
    """render a specific event based on its id"""
    model = Categorys

    def get(self, request, id):
        '''Return a specific event page by id'''
        categorys = self.get_queryset().get(id=id)#Figure out how to name thow events the same name
        return render(request, 'detail.html',{
            'categorys': categorys
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

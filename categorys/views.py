from django.shortcuts import render, redirect
from .models import Category, SubCategory, Listing
from users.models import Profile
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Listing
from .forms import CommentForm
from message.models import Message
# from .forms import PageForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.template import loader

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, get_object_or_404



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


def listing_view(request, parent_or_child=None, pk=None):

    # def add_comment_to_post(request, pk):
    #     post = get_object_or_404(Listing, pk=pk)
    #     if request.method == "POST":
    #         form = CommentForm(request.POST)
    #         if form.is_valid():
    #             comment = form.save(commit=False)
    #             comment.post = post
    #             comment.author = Profile.objects.get(user=request.user)
    #             comment.author = comment.author.user
    #             print(comment.author.user)
    #             comment.save()
    #             return redirect('index_all')
    #     else:
    #         form = CommentForm()
    #     return render(request, 'categorys/add_comment_to_post.html', {'form': form})

    categories = Category.objects.filter(parent=None)

    if parent_or_child is None:
        listings = Listing.objects.all().order_by("-created")

    elif parent_or_child == 'child':
        sub_cat = SubCategory.objects.get(pk=pk)
        listings = sub_cat.listing_set.all().order_by("-created")


    elif parent_or_child == 'parent':
        listings = []
        sub_cats = Category.objects.get(pk=pk).children.all().order_by("-created")


        for sub_cat in sub_cats:
            prds = sub_cat.listing_set.all().order_by("-created")
            listings += prds
    else:
        listings = []

    messages = Message.get_messages(user=request.user)
    active_direct = None
    directs = None


    if messages:
        message = messages[0]
        active_direct = message['user'].username
        directs = Message.objects.filter(user=request.user, recipient=message['user'])
        # directs.update(is_read=True)
        for message in messages:
            if message['user'].username == active_direct:
                message['unread'] = 0


    return render(
        request,
        'categorys/listings.html',
        {'categories': categories, 'listings': listings, 'messages': messages, 'directs':directs}
    )

class PageDetailView(DetailView):
    """ Renders a specific page based on it's pk."""
    model = Listing

    def get(self, request, pk=None): #slug
        """ Returns a specific wiki page by pk. """
        post = self.get_queryset().get(pk=pk)
        return render(request, 'categorys/post.html', {
          'post': post
        })

class GridView(ListView):
    """ Renders a list of all Pages. """
    model = Listing

    def get(self, request, parent_or_child=None, pk=None, *args, **kwargs):

        messages = Message.get_messages(user=request.user)
        active_direct = None
        directs = None


        if messages:
            message = messages[0]
            active_direct = message['user'].username
            directs = Message.objects.filter(user=request.user, recipient=message['user'])
            # directs.update(is_read=True)
            for message in messages:
                if message['user'].username == active_direct:
                    message['unread'] = 0

        """ GET a list of Pages. """
        categories = Category.objects.filter(parent=None)

        if parent_or_child is None:
            listings = Listing.objects.all().order_by("-created")

        elif parent_or_child == 'child':
            sub_cat = SubCategory.objects.get(pk=pk)
            listings = sub_cat.listing_set.all().order_by("-created")

        elif parent_or_child == 'parent':
            listings = []
            sub_cats = Category.objects.get(pk=pk).children.all().order_by("-created")

            for sub_cat in sub_cats:
                prds = sub_cat.listing_set.all().order_by("-created")
                listings += prds
        else:
            listings = []

        # print("AAAAAAAA: ", messages[0]['unread'])


        return render(
            request,
            'grid.html',
            {'categories': categories, 'listings': listings, 'messages': messages, 'directs':directs}
        )


@method_decorator([login_required], name='dispatch')
class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Listing

    def get(self, request, parent_or_child=None, pk=None, *args, **kwargs):
        """ GET a list of Pages. """
        categories = Category.objects.filter(parent=None)

        if parent_or_child is None:
            listings = Listing.objects.all().order_by("-created")

        elif parent_or_child == 'child':
            sub_cat = SubCategory.objects.get(pk=pk)
            listings = sub_cat.listing_set.all().order_by("-created")

        elif parent_or_child == 'parent':
            listings = []
            sub_cats = Category.objects.get(pk=pk).children.all().order_by()#"-created"

            for sub_cat in sub_cats:
                prds = sub_cat.listing_set.all().order_by("-created")
                listings += prds
        else:
            listings = []

        messages = Message.get_messages(user=request.user)
        active_direct = None
        directs = None


        if messages:
            message = messages[0]
            active_direct = message['user'].username
            directs = Message.objects.filter(user=request.user, recipient=message['user'])
            # directs.update(is_read=True)
            for message in messages:
                if message['user'].username == active_direct:
                    message['unread'] = 0


        return render(
            request,
            'categorys/index.html',
            {'categories': categories, 'listings': listings, 'messages': messages, 'directs':directs}
        )

class PostCreateView(CreateView):
    model = Listing
    fields = ['title', 'content', 'sub_category']
    success_url = reverse_lazy('index_all')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SubCreate(CreateView):
    model = SubCategory
    fields = ['name', 'parent']
    success_url = reverse_lazy('grid')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator([login_required], name='dispatch')
class Post_edit_view(UpdateView):
    model = Listing
    fields = ['title', 'content']
    template_name = 'categorys/index.html'
    success_url = reverse_lazy('index_all')

@method_decorator([login_required], name='dispatch')
class Post_delete_view(DeleteView):

    model = Listing
    template_name = 'categorys/post_delete.html'
    success_url = reverse_lazy('index_all')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Listing, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = Profile.objects.get(user=request.user)
            comment.author = comment.author.user
            print(comment.author.user)
            comment.save()
            return redirect('index_all')
    else:
        form = CommentForm()
    return render(request, 'templates/com.html', {'form': form})

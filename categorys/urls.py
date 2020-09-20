from django.urls import path, include
from . import views
from .views import New_wiki_form, PageDetailView  #PageListView,

# app_name = 'categorys'
urlpatterns = [
    path('', views.index_view, name='index_all'),
    path('<str:parent_or_child>/<int:pk>/', views.index_view, name='index'),
    path('listings/<str:parent_or_child>/<int:pk>/',views.listing_view, name='listing'),
    path('post/<int:pk>',PageDetailView.as_view(), name='post'),
    path('form/', New_wiki_form.as_view(), name='new'),

    # path('', PageListView.as_view(), name='wiki-list-page'),
    # path('form/', New_wiki_form.as_view(), name='new'),
    # path('<str:slug>/', PageDetailView.as_view(), name='post'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('form/', New_wiki_form.as_view(), name='new'),
    ]

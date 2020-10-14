from django.urls import path, include
from . import views
from .views import New_wiki_form, PageDetailView#, PageListView
# from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from . import settings
admin.autodiscover()

# app_name = 'categorys'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('index/', views.index_view, name='index_all'),
    path('<str:parent_or_child>/<int:pk>/', views.index_view, name='index'),
    path('listings/<str:parent_or_child>/<int:pk>/',views.listing_view, name='listing'),
    path('post/<int:pk>',PageDetailView.as_view(), name='post'),
    path('form/', New_wiki_form.as_view(), name='new'),
    path('students/', views.student_view, name='students'),
    path('professionals/', views.professionals_view, name='professionals'),
    path('<int:pk>/edit/', views.Post_edit_view.as_view(), name='edit-post'),
    path('<int:pk>/delete/', views.Post_delete_view.as_view(), name='delete-post')
    # path('home/', PageDetailView.as_view(), name='home' )
]

urlpatterns += staticfiles_urlpatterns()

    # path('', PageListView.as_view(), name='wiki-list-page'),
    # path('form/', New_wiki_form.as_view(), name='new'),
    # path('<str:slug>/', PageDetailView.as_view(), name='post'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('form/', New_wiki_form.as_view(), name='new'),

"""django_project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from categories import views as category_views



# from categories import views as category_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    # path('index/', category_views.PageListView.as_view(), name='index_all'),
    path('profile-edit/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # path('', include('blog.urls')),
    # path(r'profile/<str:username>', user_views.get_user_profile),
    path('view/<slug>', user_views.ProfileDetailView.as_view(), name='profile-detail-view'),


    path('send-invite/', user_views.send_invatation, name='send-invite'),
    path('my-invites/', user_views.invites_received_view, name='my-invites-view'),
    path('all-profiles/', user_views.ProfileListView.as_view(), name='all-profiles-view'),
    path('my-invites/accept/', user_views.accept_invatation, name='accept-invite'),
    path('my-invites/reject/', user_views.reject_invatation, name='reject-invite'),
    path('to-invite/', user_views.invite_profiles_list_view, name='invite-profiles-view'),
    path('remove-friend/', user_views.remove_from_friends, name='remove-friend'),

    path('messages/', user_views.view_messages, name='messages'),
    path('message-detail', user_views.message_detail, name='message-detail')





]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

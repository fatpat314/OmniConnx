from django.urls import path, include
from accounts.views import SignUpView
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name = 'signup'),
    # path('home/', HomeView.as_view(), name = 'home'),
] 

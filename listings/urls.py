from django.urls import path
from listings.views import CategoryListView
from . import views

app_name = 'listings'
urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    # path('<int:listing_id>/', views.detail, name='detail'),
    # path('<int:listing_id>/result/', views.result, name='result'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

]

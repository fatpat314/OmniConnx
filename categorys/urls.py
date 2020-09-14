from django.urls import path
from categorys.views import CategorysListView, SubcategorysListView, CategorysDetailView
from . import views

app_name = 'categorys'
urlpatterns = [
    path('', CategorysListView.as_view(), name='categorys_list'),
    path('<int:id>/', CategorysDetailView.as_view(), name='category-details'),
    path('subcategorys/', SubcategorysListView.as_view(), name='subcategorys'),
    # path('<int:listing_id>/', views.detail, name='detail'),
    # path('<int:listing_id>/result/', views.result, name='result'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

]

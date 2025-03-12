from django.urls import path

from .apps import CatalogConfig
from .views import ProductListView, ProductDetailView, ProductTemplateView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ProductTemplateView.as_view(), name='contacts'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('home/', ProductListView.as_view(), name='product_list'),
    path('', ProductListView.as_view(), name='product_list'),
    path('form/', ProductCreateView.as_view(), name='product_form'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]
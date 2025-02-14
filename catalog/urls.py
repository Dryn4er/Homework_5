from django.urls import path

from catalog.views import ProductCreateView, ProductUpdateView, ProductDeleteView, ProductsByCategoryView
from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, ProductDetailView, ProductListView
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('', ContactsView.as_view(), name='contacts'),
    path("product_detail/<int:pk>", cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('home', ProductListView.as_view(), name='product_list'),
    path('products/create_product', ProductCreateView.as_view(), name='product_create'),
    path('products/update_product/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete_product/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('category/<int:pk>/', ProductsByCategoryView.as_view(), name='products_by_category')
]
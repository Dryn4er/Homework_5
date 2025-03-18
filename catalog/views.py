from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductForm, ProductModeratorForm
from .models import Product, Category
from .services import get_products_by_category, get_products_from_cache


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        return get_products_from_cache()


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_delete_product'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductTemplateView(TemplateView):
    model = Product
    template_name = "catalog/contacts.html"

class CategoryListView(ListView):
    model = Category
    template_name = "catalog/category_list.html"
    context_object_name = "category_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = self.get_queryset()
        return context

    def get_queryset(self):

        catalogs = cache.get("catalogs")

        if catalogs is None:
            catalogs = Category.objects.all()
            cache.set("catalogs", catalogs, 60 * 15)

        return catalogs


class CategoryProductsListView(ListView):
    model = Product
    template_name = "catalog/category_product.html"
    context_object_name = "category_products_list"

    def get_queryset(self):

        category_id = self.kwargs.get("category_id")
        self.category = get_object_or_404(Category, pk=category_id)
        return get_products_by_category(category_id)
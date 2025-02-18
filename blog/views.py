from django.db.models import F

from .models import Blog
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'preview', 'publication_sign']
    template_name = 'blog/blog_form.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('myblog:blogs_list')


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blogs_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication_sign=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        Blog.objects.filter(pk=obj.pk).update(number_of_views=F('number_of_views') + 1)
        obj.number_of_views += 1
        return obj


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog/blog_form.html'
    fields = ['content', 'publication_sign', 'title', 'preview']
    success_url = reverse_lazy('myblog:blogs_list')


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('myblog:blogs_list')
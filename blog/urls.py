from django.urls import path
from .views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = 'myblog'

urlpatterns = [
    path('myblog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('myblog/list/', BlogListView.as_view(), name='blogs_list'),
    path('myblog/detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('myblog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('myblog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]
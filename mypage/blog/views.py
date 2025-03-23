from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Blog
# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

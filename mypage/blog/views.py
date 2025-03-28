from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog/blog_create.html'
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(BlogCreateView, self).form_valid(form)
    def get_success_url(self):
        return reverse('blog_detail', kwargs={'pk': self.object.pk})
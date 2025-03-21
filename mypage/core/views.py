from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, BlogContent
from django.views.generic import ListView, DetailView
# Create your views here.
def home(request):
    return redirect('about')
def about(request):
    return render(request, 'core/about.html')
def contact(request):
    return render(request, 'core/contact.html')
def resume(request):
    return render(request, 'core/resume.html')

def portfolio(request):
    return render(request, 'core/portfolio.html')
class BlogListView(ListView):
    model = Blog
    template_name = 'core/blog.html'
    context_object_name = 'blogs'
    def get_queryset(self):
        return Blog.objects.prefetch_related("contents").select_related("created_by__profile").all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for blog in context["blogs"]:
            blog.first_text_content = blog.contents.filter(content_type="text").first()
        return context
class BlogDetailView(DetailView):
    model = Blog
    template_name = 'core/blog_detail.html'
    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['contents'] = BlogContent.objects.filter(blog=self.object)
        return context
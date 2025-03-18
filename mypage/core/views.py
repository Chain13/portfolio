from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    return redirect('about')
def about(request):
    return render(request, 'core/about.html')
def contact(request):
    return render(request, 'core/contact.html')
def resume(request):
    return render(request, 'core/resume.html')
def blog(request):
    return render(request, 'core/blog.html')
def portfolio(request):
    return render(request, 'core/portfolio.html')

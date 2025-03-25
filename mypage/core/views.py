from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
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

class SignInView(View):
    template_name = 'core/signin.html'
    
    def get(self, request):
        print(request.user, request.user.is_authenticated)
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request=request, user=user)
            return redirect('home')
        
        return redirect('signin')

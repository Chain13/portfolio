from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.views import View
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import SignInForm

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
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, self.template_name, context={'form': SignInForm()})
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        next = request.GET.get('next')
        if user is not None:
            login(request=request, user=user)
            return redirect(next or 'home')
        return redirect(next or 'signin')

    
class SignupView(View):
    template_name = 'core/signup.html'
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request=request,template_name=self.template_name)
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        next = request.GET.get('next')
        if password == confirm_password:
            user = authenticate(username=username, password=password)
            if user is None:
                user = User.objects.create_user(username=username, password=password)
                login(request=request, user=user)
            return redirect(next or 'home')
        return redirect(next or 'signup')
class SignOutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
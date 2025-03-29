from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.views import View
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import SignInForm, SignUpForm
from django.db import IntegrityError
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
        form = SignInForm(request.POST)
        next = request.GET.get('next')
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                return redirect(next or 'home')
            else:
                form.add_error(None, 'Invalid username or password')
        return render(request, self.template_name, context={'form': form})

    
class SignupView(View):
    template_name = 'core/signup.html'
    def get(self, request):

        if request.user.is_authenticated:
            return redirect('home')
        return render(request=request,template_name=self.template_name, context={'form': SignUpForm()})
    def post(self, request):
        form = SignUpForm(request.POST)
        next = request.GET.get('next')

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            terms_and_conditions = form.cleaned_data.get('terms_and_conditions')
            if password == confirm_password:
                try:
                    user = User.objects.create_user(username=username, password=password, email=email)
                    login(request=request, user=user)
                    return redirect(next or 'home')
                except IntegrityError as e:
                    form.add_error("username", 'Username already exists')
            else:
                form.add_error("password", 'Passwords do not match')
            if not terms_and_conditions:
                form.add_error(None, 'You must agree to the terms and conditions')
    
        return render(request=request,template_name=self.template_name, context={'form': form})
class SignOutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
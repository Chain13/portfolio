
from django.urls import path
from .views import home, about, contact,resume,portfolio, SignInView
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('resume/', resume, name='resume'),
    path('portfolio/', portfolio, name='portfolio'),
    path('signin/', SignInView.as_view(), name='signin'),
    
]

from django.urls import path
from .views import home, about, contact,resume,blog,portfolio
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('resume/', resume, name='resume'),
    path('blog/', blog, name='blog'),
    path('portfolio/', portfolio, name='portfolio'),
    
]

from django.urls import path
from .views import home, about, contact,resume,portfolio, BlogListView, BlogDetailView
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('resume/', resume, name='resume'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('portfolio/', portfolio, name='portfolio'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    
]
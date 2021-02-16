from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),    
    path('home/', views.home, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
]
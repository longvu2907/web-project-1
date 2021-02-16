from django.shortcuts import render, redirect
from .models import Image

def base(request):
    return redirect('/home/')

def home(request):
    return render(request, 'home.html')

def gallery(request):
    images = Image.objects.all()
    
    context = {'images': images}
    return render(request, 'gallery.html',context)

def resume(request):
    return render(request, 'resume.html')

def contact(request):
    return render(request, 'contact.html')
from django.shortcuts import render, redirect
from .models import Image
from .forms import UploadFileForm
from accounts.models import User


def base(request):
    return redirect('/home/')

def home(request):
    return render(request, 'home.html')

def gallery(request):
    cookies = request.COOKIES
    images = Image.objects.all()
    if not is_login(cookies):
        return redirect('/accounts/login/')
    context = {'images': images}
    return render(request, 'gallery.html',context)

def add_images(request):
    image = request.FILES.get('image')
    category = request.POST.get('category', False)
    upload_image = Image(category = category ,image = image)
    upload_image.save()
    context = {'image': image,'category': category}
    return render(request, 'add_images.html',context)

def resume(request):
    return render(request, 'resume.html')

def contact(request):
    return render(request, 'contact.html')

def profile(request):
    cookies = request.COOKIES                                                        
    username = cookies.get('username')
    user = User.objects.get(username = username)
    context = {'user': user}
    if request.method == 'POST':
        avatar = request.FILES.get('avatar')
        name = request.POST.get('name', default="Name")
        if avatar == None:
            user.avatar = user.avatar
        else: 
            user.avatar = avatar
        user.name = name
        user.save()
    return render(request,'profile.html', context)

def is_login(cookies):
    if 'username' and 'password' in cookies:
        return True
    return False
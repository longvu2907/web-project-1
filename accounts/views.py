from django.shortcuts import render, redirect
from .models import User

def login(request):
    cookies = request.COOKIES
    username = request.POST.get('username', False)
    password = request.POST.get('pass', False)
    users = User.objects.all()
    if request.method == 'POST':
        if User.objects.count() > 0:
            for user in users:
                if username == user.username:
                    if password == user.password:
                        check = "Đăng nhập thành công"
                        date = user.date
                        response = render(request, 'login.html', {'check': check,'date': date})
                        response.set_cookie('username', username)
                        response.set_cookie('password', password)
                        return response
                    else:
                        check = "Sai tài khoản hoặc mật khẩu"
                else:
                    check = "Sai tài khoản hoặc mật khẩu"
        else:
            check = "Sai tài khoản hoặc mật khẩu"
    else:
        check = ''
    context = {'check':check, 'cookies':cookies}
    return render(request, 'login.html', context)

def signup(request):
    cookies = request.COOKIES
    users = User.objects.all()
    test = users[2]
    username = request.POST.get('username', False)
    password = request.POST.get('pass', False)
    repassword = request.POST.get('repass', False)   
    check = ''
    if request.method == 'POST':
        if repassword == password:
            newUser = User( username = username, password = password )
            if User.objects.count() > 0:
                for user in users:
                    if username == user.username:
                        check = "Tài khoản đã tồn tại"
                        context = {'check':check, 'cookies':cookies}
                        return render(request, 'signup.html', context)
                check = "Đăng ký thành công"
                newUser.save()
                context = {'check':check, 'cookies':cookies}
                return render(request, 'signup.html', context)
            else:
                check = "Đăng ký thành công"
                newUser.save()       
        else:
            check = "Mật khẩu không trùng khớp"
    context = {'check':check, 'cookies':cookies, 'image':test.file}
    return render(request, 'signup.html', context)

def logout(request):
    cookies = request.COOKIES
    if 'username' and 'password' in cookies:
        response = redirect('/accounts/login/')
        response.delete_cookie('username')
        response.delete_cookie('password')
        return response
    else: 
        return redirect('/accounts/login/')



def add_variable_to_context(request):
    cookies = request.COOKIES
    login_status = False
    admin = False
    if is_login(cookies):
        login_status = True
        admin = cookies['admin']
    return {
        'login_status': login_status,
        'admin': admin,
    }

def is_login(cookies):
    if 'username' and 'password' in cookies:
        return True
    return False

def is_admin(cookies):
    
    if 'admin' in cookies:
        return cookies['admin']
        if cookies['admin'] == True:
            return True
    return False
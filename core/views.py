from django.shortcuts import render

def activate_user(request, uid, token):
    print('Activate user...')
    return render(request, 'activate.html', {'uid': uid, 'token': token})

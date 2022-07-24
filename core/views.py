from django.shortcuts import render

def activate_user(request, uid, token):
    return render(request, 'activate.html', {'uid': uid, 'token': token})


def free_plan(request):
    return render(request, 'planfree.html')

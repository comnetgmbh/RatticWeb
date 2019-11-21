from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from cred import views as cred_views
from django.http import HttpResponseRedirect



def home(request):
    user = None
    if request.POST:
        username = request.POST['auth-username']
        password = request.POST.get('auth-password')
        user = authenticate(request, username=username, password=password)

        if request.user.is_authenticated:
            pass

    if user is not None:
        login(request, user)
        if request.user.is_authenticated:
            print('test')
            return redirect('cred:cred_list')

    else:
        nextpage = request.GET.get('next', ' ')
        return render(request, 'home.html', {'next': nextpage})


def home_logout(request):
    logout(request)
    return render(request, 'home.html')

def handle500(request):
    return render(request, '500.html', status=500)


def handle404(request, exception):
    return render(request, '404.html', status=404)

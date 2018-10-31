from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        login(request, user)
        if user:

            return redirect('accounts:login_info')
        return render(request, 'profile.html')
    else:
        return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')


def login_info(request):
    return render(request, 'login_info.html')


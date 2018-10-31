from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def auth_login(request):
    if request.method == 'post':
        username = request.post['username']
        password = request.post['password']

        user = authenticate(request, username=username, password=password)
        login(request, user)

        return redirect('accounts:profile')
    else:
        return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')


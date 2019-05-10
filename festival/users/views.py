from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.files.storage import FileSystemStorage
from .models import User


def mypage(request):
    return render(request, 'mypage.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],
            name=request.POST.get('name'), password=request.POST['password1'], bio=request.POST['bio'],
            phone=request.POST['phone'], gender=request.POST['gender'], profile_image=request.FILES['profile_img']
            )
            if user is not None:
                auth.login(request, user)
                return redirect('http://localhost:8000/users')
    return render(request, 'signup.html') 

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('http://localhost:8000/users')
        else:
            return redirect(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        redirect('home')
    return render(request, 'home.html')



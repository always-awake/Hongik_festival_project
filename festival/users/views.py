from django.contrib import auth
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Letter
from .forms import LetterPost


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

  
def letter_post(request, user_id):
    if request.user.is_authenticated and request.method == 'POST':
        form = LetterPost(request.POST)
        if form.is_valid():
            letter = form.save(commit=False)
            letter.letter_to = get_object_or_404(User, id=user_id)
            letter.letter_from = request.user
            letter.save()
            return redirect('/posts/')
    elif request.method == 'GET':
        form = LetterPost()
        return render(request, 'letter_post.html', {'form': form})

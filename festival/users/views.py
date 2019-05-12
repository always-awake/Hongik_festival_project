from django.contrib import auth
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Letter
from .forms import LetterPost


# 마이페이지 작성
def mypage(request):
    user = request.user
    return render(request, 'mypage.html', {'user':user})

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                name=request.POST.get('name'), 
                password=request.POST['password1'], 
                profile_image=request.FILES['profile_img'],
                bio=request.POST['bio'],
                phone=request.POST['phone'], 
                gender=request.POST['gender'], 
                )
            if user is not None:
                auth.login(request, user)
                return redirect('/users/')
    return render(request, 'signup.html') 

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print(user.id)
            return redirect('/users/mypage/')
        else:
            return redirect(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/posts/')
    return render(request, 'mypage.html')

# 쪽지를 보내는 함수
def letter_post(request, user_id):
    if request.user.is_authenticated and request.method == 'POST':
        form = LetterPost(request.POST)
        if form.is_valid():
            letter = form.save(commit=False)
            letter.letter_to = get_object_or_404(User, id=user_id)
            letter.letter_from = request.user
            letter.save()
            return redirect('letters/from/')
    elif request.method == 'GET':
        form = LetterPost()
        return render(request, 'letter_post.html', {'form': form})

# 유저가 받은 쪽지함
def letter_to_list(request):
    letter_to_list = Letter.objects.filter(letter_to=request.user)
    return render(request, 'letter_to_detail.html', {'letters':letter_to_list})

# 유저가 보낸 쪽지함
def letter_from_list(request):
    letter_from_list = Letter.objects.filter(letter_from=request.user)
    return render(request, 'letter_from_detail.html', {'letters':letter_from_list})

def user_list(request):
    users = User.objects.all()
    # 페이지네이션 코드 구현
    return render(request, 'user_list.html', {'users':users})
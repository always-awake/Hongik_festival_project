from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    # 페이지네이션 코드
    return render(request, 'post_list.html', {'posts':posts})



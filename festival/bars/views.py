from django.shortcuts import render
from .models import Bar, BarLike


def bar_list(request):
    bars = Bar.objects.all()
    # 페이지네이션 코드
    return render(request, 'bar_list.html', {'bars':bars})

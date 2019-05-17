from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import Bar, BarLike


def bar_list(request):
    bars = Bar.objects.all()
    
    paginator = Paginator(bars, 4)
    page = request.GET.get('page')
    endPage = paginator.page_range
    try:
        bars = paginator.page(page)
    except PageNotAnInteger:
        bars=paginator.page(1)
    except EmptyPage:
        bars=paginator.page(paginator.num_pages)
    
    return render(request, 'bar_list.html', {'bars': bars, 'endPage':endPage})

@login_required
def bar_detail(request, bar_id):
    user = request.user
    bar = get_object_or_404(Bar, id=bar_id)
    try:
        preexisiting_like = BarLike.objects.get(creator=user, bar=bar)
        return render(request, 'detail.html', {'bar' : bar, 'preexisiting_like':preexisiting_like})
    except BarLike.DoesNotExist:
        return render(request, 'detail.html', {'bar' : bar, 'preexisiting_like':None})

@login_required
def bar_like(request, bar_id):
    user = request.user
    bar = get_object_or_404(Bar, id=bar_id)
    try:
        preexisiting_like = BarLike.objects.get(creator=user, bar=bar)
        preexisiting_like.delete()
        return redirect('/bars/' + str(bar.id) + '/detail/')
    except BarLike.DoesNotExist:
        bar_like = BarLike()
        bar_like.bar = bar
        bar_like.creator = user
        bar_like.save()
        return redirect('/bars/' + str(bar.id) + '/detail/')
    return redirect('/bars/' + str(bar.id) + '/detail/')

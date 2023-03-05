from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    """Возвращает отображение главной страницы"""
    template = 'posts/index.html'
    return render(request, template)


def group_posts(request, slug):
    """Возвращает отображение постов в группах"""
    return HttpResponse(f'Post {slug}')

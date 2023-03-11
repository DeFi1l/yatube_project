from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    """Возвращает отображение главной страницы"""
    template = 'posts/index.html'
    posts = 'Это главная страница проекта Yatube'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request):
    """Возвращает отображение постов в группах"""
    posts = 'Здесь будет информация о группах проекта Yatube'
    context = {
        posts: 'posts'
    }
    return HttpResponse(request, context)

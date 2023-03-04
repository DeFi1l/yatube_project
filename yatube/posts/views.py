from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Main Page')


def group_posts(request, slug):
    return HttpResponse(f'Post {slug}')

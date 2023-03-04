from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Main Page')


def group_posts():
    return HttpResponse("Group's Posts")
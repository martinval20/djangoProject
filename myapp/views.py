
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Index Page")

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>"% username)

def about(request):
    return HttpResponse('about')


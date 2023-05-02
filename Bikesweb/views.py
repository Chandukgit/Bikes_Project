from django import views
from django.http import HttpResponse
def Hello(requests):
    return HttpResponse("Hello world")
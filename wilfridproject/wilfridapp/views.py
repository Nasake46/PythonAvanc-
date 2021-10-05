from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    html = "<html><body><h1>Let's GOOOOOOOOOOOO</h1></body></html>"
    return HttpResponse(html)
from django.shortcuts import render
from django.http import HttpResponse
from wilfridapp.models import Website

def index(request):
    return render(request, "wilfridapp/index.html",
                  {"websites": Website.objects.all()})
from django.shortcuts import render
from django.http import HttpResponse
from wilfridapp.models import Website
from wilfridapp.models import WebsiteForm

def index(request):
    return render(request, "wilfridapp/index.html",
                  {"websites": Website.objects.all()})

def form(request):
    return render(
        request,
        "wilfridapp/form.html",
        {
            "form": WebsiteForm,
        },
    )
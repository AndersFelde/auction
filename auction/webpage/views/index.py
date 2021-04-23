from django.shortcuts import render
#  from webpage.models import TestModal


def index(request):
    return render(request, "webpage/index.html")

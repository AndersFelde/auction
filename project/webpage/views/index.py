from django.shortcuts import render
#  from webpage.models import TestModal


def index(request):
    test = "test"
    return render(request, "webpage/index.html", context={"test": test})

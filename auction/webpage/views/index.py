from django.shortcuts import render
from webpage.modules.database import Database
#  from webpage.models import TestModal


def index(request):
    db = Database()
    items = db.getAllItems()
    return render(request, "webpage/index.html", context={"items": items})

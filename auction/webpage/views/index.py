from django.shortcuts import render
from webpage.modules.database import Database
#  from webpage.models import TestModal
#  from django.contrib.messages import get_messages
from django.contrib import messages

db = Database()


def index(request):
    items = db.getAllItems()
    print(items)
    print("mordi")
    items = getBids(items)
    return render(request, "webpage/index.html", context={"items": items})


def getBids(items):
    for item in items:
        bid = db.getCurrentBidFormatted(item.id)
        item.bid = bid

    return items

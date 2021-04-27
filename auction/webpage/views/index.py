from django.shortcuts import render
from webpage.modules.database import Database
#  from webpage.models import TestModal
#  from django.contrib.messages import get_messages

db = Database()


def index(request):
    items = db.getAllItems()
    items = getBids(items, request.user.id)
    return render(request, "webpage/index.html", context={"items": items})


def getBids(items, userId):
    for item in items:
        bid = db.getCurrentBidFormatted(item.id, userId)
        item.bid = bid

    return items

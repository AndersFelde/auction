from django.shortcuts import render
from webpage.modules.database import Database

#  from webpage.models import TestModal
db = Database()


def item(request, itemId):
    print(itemId)
    item = []
    item.append(db.getItemById(itemId))
    currentBid, nextBid = getCurrentBid(itemId)
    return render(request,
                  'webpage/item.html',
                  context={
                      'itemId': itemId,
                      "items": item,
                      'currentBid': currentBid,
                      'nextBid': nextBid
                  })


def getCurrentBid(id):
    currentBid = db.getHighestBid(id)
    if currentBid == 0:
        currentBid = "N/A"
        nextBid = int(int(db.getItemById(id).price) * 1.1)
    else:
        nextBid = int(int(currentBid) * 1.1)
        currentBid = str(currentBid) + " NOK"

    return currentBid, nextBid

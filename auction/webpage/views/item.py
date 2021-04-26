from django.shortcuts import render, redirect
from django.contrib import messages
from webpage.modules.database import Database
from webpage.modules.verify import Verify

#  from webpage.models import TestModal
db = Database()
verify = Verify()


def item(request, itemId):
    if not verify.isInt(itemId) or not db.verifyItemId(itemId):
        messages.add_message(request, messages.INFO, "Id'en du oppga er feil")
        print("ID VAR FEIL")
        return redirect("/")

    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO,
                             'Vennligst logg inn for å by')
        return redirect("/logIn")

    item = []
    item.append(db.getItemById(itemId))
    item[0].bid = db.getHighestBid(itemId)
    nextBid, item[0].bid = getNextBid(item[0])
    return render(request,
                  'webpage/item.html',
                  context={
                      'itemId': itemId,
                      "items": item,
                      'nextBid': nextBid
                  })


def getNextBid(item):
    if item.bid == 0:
        nextBid = int(item.price * 1.1)
        bid = "N/A"
    else:
        nextBid = item.bid + int(item.price * 0.1)
        bid = item.bid

    return nextBid, bid

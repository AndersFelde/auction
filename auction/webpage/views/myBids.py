from django.shortcuts import render, redirect
from webpage.modules.database import Database
from django.contrib import messages

db = Database()


def myBids(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR,
                             'Du må være logget inn for å se mine bud')
        return redirect("/logIn")

    groupedBids = {}
    bids = db.getMyBids(request.user.id)

    for bid in bids:
        if isHighest(bid):
            bid.prefix = "(du)"

        groupBid(bid, groupedBids)

    print(groupedBids)

    return render(request,
                  "webpage/myBids.html",
                  context={"groupedBids": groupedBids})


def isHighest(bid):
    highestBid, highestUser = db.getHighestBidWithUser(bid.item.id)
    if bid.user.id == highestUser.id and bid.bid == highestBid:
        return True
    return False


def groupBid(bid, groupedBids):
    if bid.item.name in groupedBids:
        groupedBids[bid.item.name].append(bid)
    else:
        groupedBids[bid.item.name] = [bid]

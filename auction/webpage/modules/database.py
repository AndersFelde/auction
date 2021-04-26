from webpage.submodels.item import Item
from webpage.submodels.bid import Bid


class Database():
    def __init__(self):
        pass

    def getAllItems(self):
        return Item.objects.all()

    def getItemById(self, id):
        return Item.objects.get(id=id)

    def verifyItemId(self, id):
        return Item.objects.filter(id=id).exists()

    def bidExists(self, id):
        return Bid.objects.filter(item__id=id).exists()

    def getHighestBid(self, id):
        if self.bidExists(id):
            return Bid.objects.filter(item__id=id).order_by("-bid")[0].bid
        return 0

    def getHighestBidUser(self, id):
        if self.bidExists(id):
            return Bid.objects.filter(item__id=id).order_by("-bid")[0].user
        return None

    def validateBid(self, bid, id, user):
        if not self.verifyItemId(id):
            return False

        item = self.getItemById(id)

        highestBid = self.getHighestBid(id)

        if bid <= item.price or bid <= highestBid:
            return "Må være ett høyere bud"

        if bid <= (highestBid + (item.price * 0.03)):
            return f"Må øke med mer enn {int(item.price * 0.03)},-"

        highestUser = self.getHighestBidUser(id)

        if highestUser == user:
            return "Kan ikke overby deg selv"

        return True

    def setNewBid(self, bid, id, user):
        item = self.getItemById(id)
        bid = Bid(item=item, bid=bid, user=user)
        bid.save()

    def getCurrentBidFormatted(self, id):
        currentBid = self.getHighestBid(id)
        if currentBid == 0:
            formattedBid = "N/A"
        else:
            formattedBid = str(currentBid) + " NOK"

        return formattedBid

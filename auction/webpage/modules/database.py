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

    def validateBid(self, bid, id):
        if not self.verifyItemId(id):
            return False

        item = self.getItemById(id)
        highestBid = self.getHighestBid(id)
        if bid > item.price and bid > highestBid and bid > (
                highestBid + (item.price * 0.03)):
            return True
        return False

    def setNewBid(self, bid, id):
        item = self.getItemById(id)
        bid = Bid(item=item, bid=bid)
        bid.save()

    def getCurrentBidFormatted(self, id):
        currentBid = self.getHighestBid(id)
        if currentBid == 0:
            formattedBid = "N/A"
        else:
            formattedBid = str(currentBid) + " NOK"

        return formattedBid

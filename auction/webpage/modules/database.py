from webpage.submodels.item import Item
from webpage.submodels.bid import Bid
from webpage.submodels.notification import Notification


class Database():
    def __init__(self):
        pass

    def getAllItems(self):
        return Item.objects.all()

    def getItemById(self, id):
        return Item.objects.get(id=id)

    def verifyItemId(self, id):
        return Item.objects.filter(id=id).exists()

    def getMyBids(self, id):
        return Bid.objects.filter(user__id=id).order_by("-dato")

    def bidExists(self, id):
        return Bid.objects.filter(item__id=id).exists()

    def getHighestBid(self, id):
        if self.bidExists(id):
            return Bid.objects.filter(item__id=id).order_by("-bid")[0].bid
        return 0

    def getHighestBidWithUser(self, id):
        if self.bidExists(id):
            bid = Bid.objects.filter(item__id=id).order_by("-bid")[0]
            return bid.bid, bid.user
        return 0, None

    def setNewBid(self, bid, id, user):
        item = self.getItemById(id)
        bid = Bid(item=item, bid=bid, user=user)
        bid.save()

    def getCurrentBidFormatted(self, id, userId):
        currentBid, userBid = self.getHighestBidWithUser(id)

        if currentBid == 0:
            formattedBid = "N/A"
        else:
            formattedBid = str(currentBid) + " NOK"
            if userBid.id == userId:
                formattedBid += " (du)"

        return formattedBid

    def getNotifications(self, userId):
        return Notification.objects.filter(user__id=userId).order_by(
            "read", "-dato")

    def getNotificationCount(self, userId):
        return Notification.objects.filter(user__id=userId, read=False).count()

    def createNotification(self, item, user, bid):
        notifi = Notification(item=item, user=user, bid=bid)
        notifi.save()

    def readNotification(self, userId, itemId):
        notifications = Notification.objects.filter(user__id=userId,
                                                    item__id=itemId,
                                                    read=False)
        print(notifications)

        for notifi in notifications:
            notifi.read = True
            notifi.save()

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from webpage.modules.database import Database
from webpage.modules.verify import Verify


class BidConsumer(AsyncWebsocketConsumer):
    db = Database()
    verify = Verify()

    async def connect(self):
        self.user = self.scope["user"]

        if self.user.is_authenticated:
            self.roomId = self.scope['url_route']['kwargs']['itemId']
            self.roomGroupId = 'item_%s' % self.roomId
            await self.channel_layer.group_add(self.roomGroupId,
                                               self.channel_name)
            await self.accept()

    async def disconnect(self, _):
        await self.channel_layer.group_discard(self.roomGroupId,
                                               self.channel_name)

    async def sendError(self, msg):
        await self.send(text_data=json.dumps({'bid': False, "msg": msg}))

    async def receive(self, text_data):
        if not self.verifyUser():
            return

        text_data_json = json.loads(text_data)
        bid = text_data_json['bid']
        if not self.verify.isInt(bid):
            await self.sendError("Please send a number")
            return

        bid = int(bid)

        validateBid = await self.validateBid(bid)

        if validateBid == True:
            # Fordi den retunerer en string hvis det er error, noe som også vil være true
            await database_sync_to_async(self.db.setNewBid)(bid, self.roomId,
                                                            self.user)
            await self.channel_layer.group_send(self.roomGroupId, {
                'type': 'newBid',
                'bid': bid,
                'userId': self.user.id
            })

            if not self.bidUser == None:
                await self.notifyBidder(bid)
        else:
            await self.sendError(validateBid)

    async def newBid(self, event):
        if self.verifyUser():
            bid = event["bid"]
            isUser = self.user.id == event["userId"]
            await self.send(text_data=json.dumps({'bid': bid, 'user': isUser}))

    async def verifyUser(self):
        if not self.user.is_authenticated:
            print(self.user + " is invalid")
            await self.send(text_data=json.dumps({
                'bid': False,
                'invalid': True
            }))
            await self.disconnect("")
            return False
        return True

    async def notifyBidder(self, bid):
        userGroupId = 'userNotify_%s' % self.bidUser.id

        await self.channel_layer.group_add(userGroupId, self.channel_name)
        print(self.channel_name)

        await self.channel_layer.group_send(
            userGroupId, {
                'type': 'notifyBid',
                'bid': bid,
                'itemId': self.roomId,
                'itemName': self.bidItem.name
            })

        await self.channel_layer.group_discard(userGroupId, self.channel_name)

        await self.createNotification(bid)

    async def notifyBid(self, _):
        pass

    @database_sync_to_async
    def createNotification(self, bid):
        self.db.createNotification(self.bidItem, self.bidUser, bid)

    @database_sync_to_async
    def validateBid(self, bid):
        if not self.db.verifyItemId(self.roomId):
            return False

        self.bidItem = self.db.getItemById(self.roomId)

        highestBid, self.bidUser = self.db.getHighestBidWithUser(self.roomId)

        if bid <= self.bidItem.price or bid <= highestBid:
            return "Må være ett høyere bud"

        if bid <= (highestBid + (self.bidItem.price * 0.03)):
            return f"Må øke med mer enn {int(self.bidItem.price * 0.03)},-"

        if not self.bidUser == None and self.bidUser.id == self.user.id:
            return "Kan ikke overby deg selv"

        return True

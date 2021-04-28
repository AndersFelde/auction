import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from webpage.modules.database import Database
from webpage.modules.verify import Verify


class NotificationConsumer(AsyncWebsocketConsumer):

    verify = Verify()
    db = Database()

    async def connect(self):
        self.user = self.scope["user"]

        if self.user.is_authenticated:
            self.path = self.scope['url_route']['kwargs']['path']
            self.roomId = self.user.id
            self.roomGroupId = 'userNotify_%s' % self.roomId

            await self.channel_layer.group_add(self.roomGroupId,
                                               self.channel_name)

            print("user joined " + self.roomGroupId)
            await self.accept()

    async def disconnect(self, _):
        await self.channel_layer.group_discard(self.roomGroupId,
                                               self.channel_name)

    #  async def sendError(self, msg):
    #      await self.send(text_data=json.dumps({'bid': False, "msg": msg}))

    async def receive(self, text_data):
        pass
        #  if not self.verifyUser():
        #      return
        #
        #  text_data_json = json.loads(text_data)
        #  msg = text_data_json['msg']
        #
        #  if validateBid == True:
        #      # Fordi den retunerer en string hvis det er error, noe som også vil være true
        #      await database_sync_to_async(self.db.setNewBid)(bid, self.roomId,
        #                                                      self.user)
        #      await self.channel_layer.group_send(self.roomGroupId, {
        #          'type': 'newBid',
        #          'bid': bid,
        #          'userId': self.user.id
        #      })
        #  else:
        #      await self.sendError(validateBid)

    async def notifyBid(self, event):
        if self.verifyUser():
            bid = event["bid"]
            if not bid == self.path:
                itemId = event["itemId"]
                itemName = event["itemName"]

                msg = f"Nytt bud: {bid}NOK, på <a href='/item/{itemId}'>{itemName}</a>"

                await self.send(text_data=json.dumps({
                    'msg': msg,
                    'itemId': itemId
                }))
                self.db.readNotification()

    async def verifyUser(self):
        if not self.user.is_authenticated:
            print(self.user + " is invalid")
            #  await self.send(text_data=json.dumps({
            #      'bid': False,
            #      'invalid': True
            #  }))
            await self.disconnect("")
            return False
        return True

    @database_sync_to_async
    def validateBid(self, bid):
        if not self.db.verifyItemId(self.roomId):
            return False

        item = self.db.getItemById(self.roomId)
        self.bidItemName = item.name

        highestBid, self.bidUserId = self.db.getHighestBidWithUser(self.roomId)

        if bid <= item.price or bid <= highestBid:
            return "Må være ett høyere bud"

        if bid <= (highestBid + (item.price * 0.03)):
            return f"Må øke med mer enn {int(item.price * 0.03)},-"

        if self.bidUserId == self.user.id:
            return "Kan ikke overby deg selv"

        return True

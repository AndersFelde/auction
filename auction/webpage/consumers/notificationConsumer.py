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

    async def receive(self, _):
        pass

    async def notifyBid(self, event):
        if self.verifyUser():
            bid = event["bid"]
            itemId = event["itemId"]
            print(itemId, self.path)
            if not itemId == self.path:
                itemName = event["itemName"]

                msg = f"Nytt bud: {bid}NOK, på <a href='/item/{itemId}'>{itemName}</a>"

                await self.send(text_data=json.dumps({
                    'msg': msg,
                    'itemId': itemId
                }))
            else:
                await self.readNotification(itemId)

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
    def readNotification(self, itemId):
        self.db.readNotification(self.user.id, itemId)

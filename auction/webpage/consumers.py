import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .modules.database import Database
from .modules.verify import Verify


class ChatConsumer(AsyncWebsocketConsumer):
    db = Database()
    verify = Verify()

    async def connect(self):
        self.roomId = self.scope['url_route']['kwargs']['itemId']
        self.roomGroupId = 'item_%s' % self.roomId
        self.user = self.scope["user"]

        # Join room group
        if self.user.is_authenticated:
            await self.channel_layer.group_add(self.roomGroupId,
                                               self.channel_name)
            await self.accept()

    async def disconnect(self, _):
        await self.channel_layer.group_discard(self.roomGroupId,
                                               self.channel_name)

    async def sendError(self, msg):
        await self.send(text_data=json.dumps({'bid': False, "msg": msg}))

    async def receive(self, text_data):
        if not self.user.is_authenticated:
            await self.disconnect("")

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
                'bid': bid
            })
        else:
            await self.sendError(validateBid)

    async def newBid(self, event):
        if not self.user.is_authenticated:
            await self.disconnect("")
        bid = event["bid"]
        await self.send(text_data=json.dumps({'bid': bid}))

    @database_sync_to_async
    def validateBid(self, bid):
        return self.db.validateBid(bid, self.roomId, self.user)

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .submodels.log import Log
from .submodels.item import Item
from .submodels.bid import Bid
from .modules.database import Database


class ChatConsumer(AsyncWebsocketConsumer):
    db = Database()

    async def connect(self):
        self.roomId = self.scope['url_route']['kwargs']['itemId']
        self.roomGroupId = 'item_%s' % self.roomId

        # Join room group
        await self.channel_layer.group_add(self.roomGroupId, self.channel_name)
        await self.accept()

    async def disconnect(self, _):
        await self.channel_layer.group_discard(self.roomGroupId,
                                               self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        bid = text_data_json['bid']

        isHigher = await self.higherBid(bid)

        if isHigher:
            self.db.setNewBid(bid, id)
            await self.channel_layer.group_send(self.roomGroupId, {
                'type': 'newBid',
                'bid': bid
            })
        else:
            await self.send(text_data=json.dumps({'bid': False}))

    async def newBid(self, event):
        bid = event["bid"]
        await self.send(text_data=json.dumps({'bid': bid}))

        #  await self.addLog(message)

    @database_sync_to_async
    def higherBid(self, bid):
        return self.db.validateBid(bid, self.roomId)

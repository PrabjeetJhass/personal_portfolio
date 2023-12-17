import json
from channels.generic.websocket import AsyncWebsocketConsumer
 
class Notify_consumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "notifications"
        await self.channel_layer.group_add(
            self.roomGroupName ,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self , close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName , 
            self.channel_name 
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(self.scope['user'].username)
        message = text_data_json.get("message")
        sender = self.scope['user'].username
        receiver = text_data_json["username"]
        await self.channel_layer.group_send(
            self.roomGroupName,{
                "type" : "sendMessage" ,
                'sender': sender,
                'receiver': receiver,
            })

    async def sendMessage(self , event):
        receiver = event['receiver']
        sender = event['sender']
        username = self.scope['user'].username

        if username == receiver:
            message = f'{sender} just poked you!'
            await self.send(text_data = json.dumps({"message": message}))
        
        if username == sender:
            message = f'You just poked {receiver}'
            await self.send(text_data=json.dumps({'message': message}))
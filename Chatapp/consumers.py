import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import *

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = f"room_{self.scope['url_route']['kwargs']['room_name']}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json

    # Create event and send to all group members
        event = {
            'type': 'send_message',
            'message': message,
        }

    # Broadcast message to the group
        await self.channel_layer.group_send(self.room_name, event)

    async def send_message(self, event):
        
        data = event['message']

        # Store message in the database
        await self.create_message(data=data)

        # Prepare data to send to all clients
        response_data = {
            'sender': data['sender'],
            'message': data['message']
        }

        # Send the message to all connected WebSocket clients
        await self.send(text_data=json.dumps({'message': response_data}))

    @database_sync_to_async
    def create_message(self, data):

        get_room_by_name = Room.objects.get(room_name=data['room_name'])
        
        if not Message.objects.filter(message=data['message']).exists():
            new_message = Message(room=get_room_by_name, sender=data['sender'], message=data['message'])
            new_message.save()  
        
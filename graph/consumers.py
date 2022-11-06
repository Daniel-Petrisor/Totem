import os
import time
from time import sleep
from random import randint

import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

# from channels.generic.websocket import AsyncWebsocketConsumer



class ChatConsumers(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        print("connect")

        # self.send(text_data=json.dumps({
        #     'type': 'connection_enstablished',
        #     'message': current_file
        # }))



    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # message = current_file

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message': message
            }
        )
        print("receive")




    def chat_message(self, event):
        message = event['message']
        # message = current_file
        
        print('Message', message)

        self.send(text_data=json.dumps({
            'type':'chat',
            'message': message
        }))
        print("chat_message")



    def disconnect(self, close_code):
        print("closed")
        return super().disconnect(close_code)


# class DashConsumer(AsyncWebsocketConsumer):
    
#     async def connect(self):
#         self.groupname='dashboard'
#         await self.channel_layer.group_add(
#             self.groupname,
#             self.channel_name,
#         )

#         await self.accept()
#         for i in range(100):
#             # value >>> main.js file
#             self.send(json.dumps({'value': randint(100, 120)}))
#             await sleep(1)


#     async def disconnect(self,close_code):

#         await self.channel_layer.group_discard(
#             self.groupname,
#             self.channel_name
#         )
    

#     async def receive(self, text_data):
#         datapoint = json.loads(text_data)
#         val =datapoint['value']

#         await self.channel_layer.group_send(
#             self.groupname,
#             {
#                 'type':'deprocessing',
#                 'value':val
#             }
#         )

#         print ('>>>>',text_data)

#         # pass

#     async def deprocessing(self,event):
#         valOther=event['value']
#         await self.send(text_data=json.dumps({'value':valOther}))
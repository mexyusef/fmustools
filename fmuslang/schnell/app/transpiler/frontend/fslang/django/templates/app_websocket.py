import json, time
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class __TEMPLATE_TABLENAME_CASE__Consumer(WebsocketConsumer):
  def connect(self):
    self.room_name = self.scope['url_route']['kwargs']['room_name']
    self.room_group_name = '__TEMPLATE_TABLENAME_LOWER___%s' % self.room_name
    async_to_sync(self.channel_layer.group_add)(
      self.room_group_name,
      self.channel_name
    )
    self.accept()
    self.after_connect()
  def disconnect(self, close_code):
    async_to_sync(self.channel_layer.group_discard)(
      self.room_group_name,
      self.channel_name
    )
  def receive(self, text_data):
    text_data_json = json.loads(text_data)
    message = text_data_json['message']
    async_to_sync(self.channel_layer.group_send)(
      self.room_group_name,
      {
        'type': '__TEMPLATE_TABLENAME_LOWER___message',
        'message': message
      }
    )
  def send_individual(self, data):
    async_to_sync(self.channel_layer.send)(self.channel_name, data)
  def send_group(self, data):
    async_to_sync(self.channel_layer.group_send)(self.room_group_name, data)
  def __TEMPLATE_TABLENAME_LOWER___message(self, event):
    message = event['message']
    data = event['data']
    self.send(text_data=json.dumps({
      'message': message,
      'data': data,
    }))
  def after_connect(self):
    time.sleep(0.2)
    print('client connected.')

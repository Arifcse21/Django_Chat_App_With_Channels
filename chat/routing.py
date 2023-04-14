from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/chat/(?P<room_name>\w+)/setting$', consumers.ChatConsumer3.as_asgi()),
    re_path(r'ws$', consumers.ChatConsumerx.as_asgi()),
    re_path(r'', consumers.ChatConsumer2.as_asgi()),
]
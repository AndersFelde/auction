from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/(?P<itemId>\w+)/$', consumers.ChatConsumer.as_asgi()),
]

from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/bid/(?P<itemId>\w+)/$', consumers.BidConsumer.as_asgi()),
]

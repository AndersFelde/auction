from django.urls import re_path

from .consumers.bidConsumer import BidConsumer
from .consumers.notificationConsumer import NotificationConsumer

websocket_urlpatterns = [
    re_path(r'ws/bid/(?P<itemId>\w+)/$', BidConsumer.as_asgi()),
    re_path(r'ws/notify/(?P<path>\w+)$', NotificationConsumer.as_asgi()),
    #  re_path(r'ws/notify/(?P<path>\w+)/$', NotificationConsumer.as_asgi()),
    #  re_path(r"^ws/notify/$", NotificationConsumer.as_asgi()),
]

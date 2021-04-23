"""
ASGI config for auction auction.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoauction.com/en/3.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import webpage.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auction.settings')

application = ProtocolTypeRouter({
    "http":
    get_asgi_application(),
    "websocket":
    AuthMiddlewareStack(URLRouter(webpage.routing.websocket_urlpatterns))
})

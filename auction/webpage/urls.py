from django.urls import path
from .views import index, room

urlpatterns = [
    path("", index.index, name="index"),
    path("room/<str:room_name>", room.room, name="room"),
]

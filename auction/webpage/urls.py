from django.urls import path
from .views import index, item

urlpatterns = [
    path("", index.index, name="index"),
    path("item/<str:itemId>", item.item, name="item"),
]

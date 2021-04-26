from django.urls import path, re_path
from django.views.generic.base import RedirectView
from .views import index, item

urlpatterns = [
    path("", index.index, name="index"),
    path("item/<str:itemId>", item.item, name="item"),
    re_path(r'^.*$',
            RedirectView.as_view(url='/', permanent=False),
            name='index')
]

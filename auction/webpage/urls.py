from django.urls import path, re_path
from django.views.generic.base import RedirectView
from .views import index, item, logIn, signUp, logOut

urlpatterns = [
    path("", index.index, name="index"),
    path("item/<str:itemId>", item.item, name="item"),
    path("logIn", logIn.logIn, name="logIn"),
    path("signUp", signUp.signUp, name="signUp"),
    path("logOut", logOut.logOut, name="logOut"),
    #  re_path(r'^.*$',
    #          RedirectView.as_view(url='/', permanent=False),
    #          name='index')
]

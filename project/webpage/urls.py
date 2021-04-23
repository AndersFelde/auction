from django.urls import path
from .views import index, formPage

urlpatterns = [
    path("", index.index, name="index"),
    path("formPage", formPage.formPage, name="formPage"),
]

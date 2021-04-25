from django.contrib import admin
from .submodels.log import Log
from .submodels.item import Item
#  from .submodels.model1 import Model2

admin.site.register(Log)
admin.site.register(Item)
#  admin.site.register(Model2)

# admin:admin

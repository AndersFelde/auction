from django.contrib import admin
from .submodels.log import Log
from .submodels.item import Item
from .submodels.bid import Bid
#  from .submodels.model1 import Model2

admin.site.register(Log)
admin.site.register(Item)
admin.site.register(Bid)
#  admin.site.register(Model2)

# admin:adminmodels.ForeignKey(Reporter, on_delete=models.CASCADE)

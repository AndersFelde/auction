from django.db import models
from django.utils import timezone
from .item import Item


class Bid(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    bid = models.IntegerField()
    dato = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.item.name}: {self.bid},-"

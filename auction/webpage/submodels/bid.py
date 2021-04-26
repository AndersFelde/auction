from django.db import models
from django.utils import timezone
from .item import Item
from django.contrib.auth.models import User


class Bid(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             default=11)  #Er en dummy user
    bid = models.IntegerField()
    dato = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.item.name}: {self.bid},- ({self.user.username})"

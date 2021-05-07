from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta


class Item(models.Model):

    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(upload_to="webpage/images/items/")
    dato = models.DateTimeField(default=timezone.now)
    expiration = models.DateTimeField(default=datetime.now() +
                                      timedelta(hours=9))

    def __str__(self):
        return f"{self.name}: {self.price},-"

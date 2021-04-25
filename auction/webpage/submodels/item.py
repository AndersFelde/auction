from django.db import models
from django.utils import timezone


class Item(models.Model):

    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(upload_to="webpage/images/items/")
    dato = models.DateTimeField(default=timezone.now)

    def imageName(self):
        return str(self.image).split("/")[-1]

    def __str__(self):
        return f"{self.name}: {self.price},-"

from django.db import models
from .model1 import Model1


class Model2(models.Model):
    model1 = models.ForeignKey(Model1,
                               on_delete=models.CASCADE,
                               related_name="lag")
    integer = models.IntegerField()
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

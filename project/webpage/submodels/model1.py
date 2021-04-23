from django.db import models


class Model1(models.Model):

    navn = models.CharField(max_length=15)
    draktFarge = models.CharField(max_length=20)
    bilde = models.CharField(max_length=50)

    def __str__(self):
        return self.navn

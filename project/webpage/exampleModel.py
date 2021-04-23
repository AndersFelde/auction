from django.db import models
from django.utils import timezone


class Lag(models.Model):

    navn = models.CharField(max_length=15)
    draktFarge = models.CharField(max_length=20)
    bilde = models.CharField(max_length=50)

    def __str__(self):
        return self.navn


class Side(models.Model):

    lag = models.ForeignKey(Lag, on_delete=models.CASCADE, related_name="lag")
    motstander = models.ForeignKey("self",
                                   on_delete=models.CASCADE,
                                   related_name="mot",
                                   null=True)
    poeng = models.IntegerField()
    maal = models.IntegerField()
    maal_forskjell = models.IntegerField()


class Kamp(models.Model):

    side_1 = models.ForeignKey(Side,
                               on_delete=models.CASCADE,
                               related_name="side_1")
    side_2 = models.ForeignKey(Side,
                               on_delete=models.CASCADE,
                               related_name="side_2")

    dato = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.side_1.lag.navn + "-" + self.side_2.lag.navn


class Resultat(models.Model):

    lag = models.ForeignKey(Lag, on_delete=models.CASCADE)
    antall_kamper = models.IntegerField()
    vunnet = models.IntegerField()
    tapt = models.IntegerField()
    uavgjort = models.IntegerField()
    egne_maal = models.IntegerField()
    maal_imot = models.IntegerField()
    maal_forskjell = models.IntegerField()
    poeng_sum = models.IntegerField()

    def __str__(self):
        return self.lag.navn


# Create your models here.

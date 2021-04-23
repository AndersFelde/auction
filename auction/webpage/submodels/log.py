from django.db import models


class Log(models.Model):

    room_name = models.CharField(max_length=15)
    message = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.room_name}: {self.message}"

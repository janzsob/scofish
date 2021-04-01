from django.db import models
""""
from django.contrib.auth.models import User
from new_trip.models import Trips

class Fisherman(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trips = models.ManyToManyField(Trips, blank=True)

    class Meta:
        verbose_name = 'Fisherman'
        verbose_name_plural = 'Fishermen'

    def __str__(self):
        return self.user.username
"""
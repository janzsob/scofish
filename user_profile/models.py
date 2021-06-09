from django.db import models
from new_trip.models import Fisherman

class HookBait(models.Model):
    fisherman = models.ForeignKey(Fisherman, on_delete=models.CASCADE)
    name = models.CharField("Termék neve", max_length=150)
    size = models.CharField("Méret", max_length=100)
    taste = models.CharField("Íz", max_length=80)


    class Meta:
        verbose_name = "HookBait"
        verbose_name_plural = "HookBaits"

    def __str__(self):
        return self.name

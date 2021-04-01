from django.db import models


class Trips(models.Model):
    place = models.CharField("Place", max_length=100)
    s_date = models.DateTimeField("Starting Date", auto_now=False, auto_now_add=False)
    e_date = models.DateTimeField("Ending Date", auto_now=False, auto_now_add=False)
    trip_id = models.AutoField(primary_key=True)    

    class Meta:
        verbose_name = "Trip"
        verbose_name_plural = "Trips"

    def __str__(self):
        return f"{self.place}-{self.trip_id}"


class Fisherman(models.Model):
    name = models.CharField("Fisherman", max_length=50)
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)
    fisherman_id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = "Fisherman"
        verbose_name_plural = "Fishermen"

    def __str__(self):
        return f"{self.name}-{self.fisherman_id}"

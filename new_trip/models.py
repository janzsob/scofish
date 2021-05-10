from django.db import models
from django.contrib.auth.models import User


class Fisherman(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fisherman_id = models.AutoField(primary_key=True)
    catch_sum_weight = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Fisherman"
        verbose_name_plural = "Fishermen"

    def __str__(self):
        return self.user.username



class Trips(models.Model):
    lake = models.CharField("Lake", max_length=150)
    city = models.CharField("City", max_length=100, blank=True)
    s_date = models.DateTimeField("Starting Date", auto_now=False, auto_now_add=False)
    e_date = models.DateTimeField("Ending Date", auto_now=False, auto_now_add=False)
    fisherman = models.ManyToManyField(Fisherman)
    trip_id = models.AutoField(primary_key=True)
    total_catch_weight = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    num_of_fish = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Trip"
        verbose_name_plural = "Trips"

    def __str__(self):
        return f"{self.lake}-{self.trip_id}-{self.s_date}"



fish_choices = [
    ("Ponty", "Ponty"),
    ("Amur", "Amur"),
    ("Keszeg", "Keszeg"),
    ("Kárász", "Kárász"),
    ("Harcsa", "Harcsa"),
    ("Tok", "Tok"),
]


class Catch(models.Model):
    fish_type = models.CharField("Fish Type", max_length=50, choices=fish_choices, default="Carp")
    catch_id = models.AutoField(primary_key=True)
    weight = models.DecimalField("Weight", max_digits=5, decimal_places=2)
    length = models.DecimalField("Length", max_digits=5, decimal_places=2, blank=True, null=True)
    hook_bait = models.CharField("Hook Bait", max_length=100)
    datetime = models.DateTimeField("Catch Time", auto_now=False, auto_now_add=False)
    image = models.ImageField(null=True, blank=True, upload_to="catch_images/")
    fisherman = models.ForeignKey(Fisherman, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Catch"
        verbose_name_plural = "Catches"

    def __str__(self):
        return f"{self.fish_type}-{self.catch_id}"
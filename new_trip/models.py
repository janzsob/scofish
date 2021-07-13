from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django_resized import ResizedImageField
#from PIL import Image
#from .utils import image_resize

class Fisherman(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fisherman_id = models.AutoField(primary_key=True)
    catch_sum_weight = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Fisherman"
        verbose_name_plural = "Fishermen"

    def __str__(self):
        return f'{self.user.username}'



class Trips(models.Model):
    lake = models.CharField("Lake", max_length=150)
    city = models.CharField("City", max_length=100, blank=True)
    s_date = models.DateTimeField("Starting Date", auto_now=False, auto_now_add=False)
    e_date = models.DateTimeField("Ending Date", auto_now=False, auto_now_add=False)
    fisherman = models.ManyToManyField(Fisherman)
    trip_id = models.AutoField(primary_key=True)
    total_catch_weight = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    # it defines whether the trip is active or not.
    @property
    def is_active(self):
        if self.e_date.strftime('%Y/%m/%d %H:%M') > datetime.now().strftime('%Y/%m/%d %H:%M'):
            return True
        return False
    
    class Meta:
        verbose_name = "Trip"
        verbose_name_plural = "Trips"

    def __str__(self):
        return f"{self.lake} - {self.trip_id} - {self.s_date.strftime('%Y/%m/%d')}"



class HookBait(models.Model):
    hookbait_id = models.AutoField(primary_key=True)
    name = models.CharField('HookBait', max_length=120, blank=True, null=True)
    fisherman = models.ForeignKey(Fisherman, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Hookbait"
        verbose_name_plural = "Hookbaits"

    def __str__(self):
        return self.name


# Choices for catch
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
    datetime = models.DateTimeField("Catch Time", auto_now=False, auto_now_add=False)
    image = ResizedImageField(size=[1080, 1350], quality=95, keep_meta=False, null=True, blank=True, default="default_img.png", upload_to="catch_images/")
    fisherman = models.ForeignKey(Fisherman, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)
    hookbait_name = models.CharField('Csali megnevezése', max_length=120, blank=True, null=True)
    hookbait = models.ForeignKey(HookBait, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = "Catch"
        verbose_name_plural = "Catches"

    def __str__(self):
        return f"{self.fish_type}, {self.weight} kg - {self.trip.lake} - {self.datetime.strftime('%Y/%m/%d, %H:%M')}"

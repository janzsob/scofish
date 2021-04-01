"""
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Fisherman

@receiver(post_save, sender=User)
def create_fisherman(sender, instance, created, **kwargs):
    if created:
        Fisherman.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_fisherman(sender, instance, **kwargs):
    instance.fisherman.save()
"""





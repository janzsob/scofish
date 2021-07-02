from django.contrib import admin
from .models import Trips, Fisherman, Catch, HookBait

admin.site.register(Trips)
admin.site.register(Fisherman)
admin.site.register(Catch)
admin.site.register(HookBait)

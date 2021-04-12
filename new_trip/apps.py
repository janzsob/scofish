from django.apps import AppConfig


class NewTripConfig(AppConfig):
    name = 'new_trip'

    def ready(self):
        import new_trip.signals
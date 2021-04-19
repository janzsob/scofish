from django.shortcuts import render
from django.views.generic.list import ListView
from new_trip.models import Trips, Fisherman
from django.db.models import Count, Sum
import datetime



class FeedView(ListView):
    model = Trips
    template_name = "trips_feed/feed.html"
    context_object_name = "trips"
    ordering = ['-trip_id']
    #queryset = Trips.objects.all().annotate(
    #    catch_count=Count("catch", distinct=True), # To count the number of catches
    #    fisherman_count=Count('fisherman', distinct=True) # To count the number of fishermen in the trip
    #)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_date"] = datetime.datetime.now()
        return context
    
    

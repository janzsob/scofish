from django.shortcuts import render
from django.views.generic.list import ListView
from new_trip.models import Trips, Fisherman, Catch
from django.db.models import Count, Sum
import datetime
from django.views.generic.base import TemplateView


class FeedView(ListView):
    model = Trips
    template_name = "trips_feed/feed.html"
    context_object_name = "trips"
    ordering = ['-trip_id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_date"] = datetime.datetime.now()
        # to get access each trip pk
        sum_list = []
        for t in context["trips"]:
            total_catches = Catch.objects.filter(trip=t).aggregate(s_weight=Sum('weight'))
            sum_list.append(
                total_catches["s_weight"]
            )
        context["sum_list"] = sum_list

        return context


class HomeView(TemplateView):
    template_name = "trips_feed/home.html"
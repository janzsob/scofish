from django.shortcuts import render
from new_trip.models import Catch
from django.views.generic.detail import DetailView


class CatchView(DetailView):
    model = Catch
    template_name = "catch_details/catch.html"
    context_object_name = "catch"

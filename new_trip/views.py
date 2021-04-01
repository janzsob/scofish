from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import TripsForm, FishermanFormset


def create_trip_view(request):
    if request.method == "POST":
        trip_form = TripsForm(request.POST)
        formset = FishermanFormset(request.POST)
        if trip_form.is_valid() and formset.is_valid():
            if trip_form.cleaned_data:
                trip = trip_form.save()
            for formset_user in formset:
                user = formset_user.save(commit=False)
                user.trip = trip
                user.save()
            return redirect("auth:home")
    else:
        trip_form = TripsForm()
        formset = FishermanFormset()   
    context = {
        "trip_form": trip_form,
        "formset": formset
    }
    return render(request, "new_trip/create_trip.html", context)

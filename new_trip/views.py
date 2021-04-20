from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import TripsForm, CatchForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Trips, Fisherman, Catch
from django.contrib.auth.decorators import login_required


@login_required
def create_trip_view(request):
    if request.method == "POST":
        trip_form = TripsForm(request.POST)
        if trip_form.is_valid():
            if trip_form.cleaned_data:
                trip = trip_form.save()
            return redirect(reverse("new_trip:trip_details", args=(trip.trip_id,)))
    else:
        trip_form = TripsForm()
    context = {
        "trip_form": trip_form,
    }
    return render(request, "new_trip/create_trip.html", context)


class TripDetailView(DetailView):
    model = Trips
    template_name = "new_trip/trip_details.html"
    context_object_name = "trip"

    # get catches in the trip
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["catches"] = Catch.objects.filter(trip=self.kwargs.get('pk')).order_by('datetime')

        return context

    """
    For modal
    def post(self, *args, **kwargs):
        self.object = self.get_object(self.get_queryset())
        catch_form = CatchForm(self.request.POST)
        if catch_form.is_valid():
            if catch_form.cleaned_data:
                catch_form.instance.trip = self.object
                catch_form.save()
                return redirect(reverse("auth:home"))
            else:
                catch_form = CatchForm()
    """             

"""
def new_catch(request):
    if request.method == "POST":
        catch_form = CatchForm(request.POST)
        if catch_form.is_valid():
            if catch_form.cleaned_data:
                catch = catch_form.save()
            return redirect(reverse("auth:home"))
    else:   
        catch_form = CatchForm()
    context = {
        "catch_form": catch_form,
    }
    return render(request, "new_trip/trip_details.html", context)
"""

@login_required
class NewCatchView(CreateView):
    model = Catch
    form_class = CatchForm
    template_name = "new_trip/new_catch.html"
    
    # It lists those fishermen who attend at the trip
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['fisherman'] = Fisherman.objects.filter(trips__trip_id=self.kwargs.get('pk'))
        return kwargs
    
    def form_valid(self, form):
        # It makes catch equal to the trip
        current_trip = Trips.objects.get(pk=self.kwargs['pk'])
        form.instance.trip = current_trip

        # to add weight of the new catch to the total weight in Trips
        current_trip.total_catch_weight += form.instance.weight
        current_trip.save()

        # It adds cacth to the Fishermen total cacthes
        catcher = Fisherman.objects.get(fisherman_id=form.instance.fisherman_id) # by adding _id to the object, it gives the id
        catcher.catch_sum_weight += form.instance.weight
        catcher.save()

        # number of catches in Trips
        current_trip.num_of_fish += 1
        current_trip.save()

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('new_trip:trip_details', args=(self.kwargs['pk'],))


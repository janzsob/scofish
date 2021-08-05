from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import TripsForm, CatchForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Trips, Fisherman, Catch, HookBait
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView
from datetime import datetime

"""
#@login_required
def create_trip_view(request):
    if not request.user.is_authenticated:
            messages.info(request, 'Jelentkezz be az új túra létrehozásához.')
            return redirect("auth:login")
    
    actual_fisherman = request.user.fisherman
    for trip in actual_fisherman.trips_set.all():
        if trip.is_active == True:
            var = True
            return var
    if var:
        print("OK")
    else:
        if request.method == "POST":
            trip_form = TripsForm(request.POST)
            if trip_form.is_valid():
                if trip_form.cleaned_data:
                    trip = trip_form.save()
                return redirect(reverse("new_trip:trip_details", args=(trip.trip_id,)))
        else:
            trip_form = TripsForm()
        context = {
            "form": trip_form,
        }
        return render(request, "new_trip/create_trip.html", context)
"""

# Custom LoginRequiredMixin is needed to add alert message.
class CreateTripLoginRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, 'Jelentkezz be az új horgászat létrehozásához.')
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class CreateTripView(CreateTripLoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Trips
    form_class = TripsForm
    template_name = "new_trip/create_trip.html"
    success_message = "Horgásztúra sikeresen létrehozva."

    # it checks whether user has an active trip
    def has_active_trip(self):
        fisherman = self.request.user.fisherman
        for trip in fisherman.trips_set.all():
            if trip.is_active == True:
                return True
        return False

    # user is not able to create a new trip if he/she has already an existing one.
    def get(self, request, *args, **kwargs):
        if self.has_active_trip():
            # get id of the active trip
            active_trip_id = 0
            fisherman = self.request.user.fisherman
            for trip in fisherman.trips_set.all():
                if trip.is_active == True:
                    active_trip_id = trip.trip_id
                        
            messages.error(request, 'Van már egy aktív horgászatod.')
            return redirect('new_trip:trip_details', pk=active_trip_id)
        else:
            return super().get(request, *args, **kwargs)

    # checks whether any fishermen have an active trip. If yes the new trip cannot be created.
    def form_valid(self, form):
        for fisherman in form.cleaned_data["fisherman"]:
            for trip in fisherman.trips_set.all():
                if trip.is_active == True:
                    messages.error(self.request, 'Az egyik résztvevőnek van már aktív horgásztúrája.')
                    return redirect("trips_feed:feed")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('new_trip:trip_details', args=(self.object.trip_id,))


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

# Custom LoginRequiredMixin for new catch.
class NewCatchLoginRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, 'Jelentkezzen be a fogás rögzítéséhez.')
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class NewCatchView(NewCatchLoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Catch
    form_class = CatchForm
    template_name = "new_trip/new_catch.html"
    success_message = "Fogás rögzítve"
    
    # It checks whether the request user is in the trip.
    def is_in_trip(self):
        fishermen_in_trip = Fisherman.objects.filter(trips__trip_id=self.kwargs.get('pk'))
        for man in fishermen_in_trip:
            if man == self.request.user.fisherman:
                return True
        return False

    # It checks whether the fishing trip has ended.
    def is_trip_open(self):
        trip = Trips.objects.filter(trip_id=self.kwargs.get('pk'))
        for t in trip:
            if t.is_active == True:
                return True
        return False

    def get(self, request, *args, **kwargs):
        # checks whether the trip is open
        if self.is_trip_open():
            # checks wether the user in the trip
            if self.is_in_trip():
                return super().get(request, *args, **kwargs)
            else:
                messages.error(request, 'Nem rögzíhetsz fogást más horgászatán.')
                return redirect('new_trip:trip_details', pk=self.kwargs.get('pk'))
        else:
            messages.error(request, 'A horgászat lezárult. Már nem tudsz új fogásokat rögzíteni.')
            return redirect('new_trip:trip_details', pk=self.kwargs.get('pk'))
                
        
    # It lists those fishermen who attend at the trip
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['fisherman'] = Fisherman.objects.filter(trips__trip_id=self.kwargs.get('pk'))
        return kwargs
    
    def form_valid(self, form):
        # It makes catch equal to the trip
        current_trip = Trips.objects.get(pk=self.kwargs['pk'])
        form.instance.trip = current_trip

        # Adding extra validation error: 
        if form.instance.hookbait_name != None and form.instance.hookbait != None:
            form.add_error("hookbait_name", "Csak egy csalit adhat meg!")
            form.add_error("hookbait", "Csak egy csalit adhat meg!")
            return super().form_invalid(form)

        # to add weight of the new catch to the total weight in Trips
        current_trip.total_catch_weight += form.instance.weight
        current_trip.save()

        # It adds cacth to the Fishermen total cacthes
        catcher = Fisherman.objects.get(fisherman_id=form.instance.fisherman_id) # by adding _id to the object, it gives the id
        catcher.catch_sum_weight += form.instance.weight
        catcher.save()

        # It creates a hookbait
        if not form.instance.hookbait_name == None:
            HookBait.objects.create(name=form.instance.hookbait_name, fisherman=form.instance.fisherman)

        if not form.instance.hookbait == None:
            form.instance.hookbait_name = form.instance.hookbait.name
            
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('new_trip:trip_details', args=(self.kwargs['pk'],))


# Ajax for dependent select on the new catch page
def load_hookbaits(request):
    fisherman_id = request.GET.get("fisherman_id") # it is coming from the jquery script in the new catch page
    hookbaits = HookBait.objects.filter(fisherman_id=fisherman_id).order_by('name')
    return render(request, "new_trip/hookbaits_dependent_select.html", {"hookbaits": hookbaits})


class TripUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Trips
    form_class = TripsForm
    template_name = "new_trip/create_trip.html"
    success_message = "Horgásztúra módosítva."

    # It limits that fishermen can only update the trips in which they are attending.
    def test_func(self):
        trip = self.get_object()
        for u in trip.fisherman.all():
            if self.request.user == u.user:
                return True
        return False

    def get_success_url(self):
        return reverse('new_trip:trip_details', args=(self.object.trip_id,))
    
"""
class TripDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Trips
    template_name = ""

    # It limits that fishermen can only update the trips in which they are attending.
    def test_func(self):
        trip = self.get_object()
        for u in trip.fisherman.all():
            if self.request.user == u.user:
                return True
        return False

    def get_success_url(self):
        return reverse('trips_feed:feed')
"""
from django.shortcuts import render, reverse
from new_trip.models import Catch, Fisherman, Trips
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView, DeleteView
from new_trip.forms import CatchForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class CatchView(DetailView):
    model = Catch
    template_name = "catch_details/catch.html"
    context_object_name = "catch"


class CatchUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Catch
    form_class = CatchForm # it gives all fields and the styling
    template_name = "new_trip/new_catch.html"
    success_message = "Fogás módosítva."

    # It lists those fishermen who attend at the trip
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['fisherman'] = Fisherman.objects.filter(trips__trip_id=self.object.trip_id)
        return kwargs

    # It limits that fishermen can only update their own catches
    def test_func(self):
        catch = self.get_object()
        if self.request.user == catch.fisherman.user:
            return True
        return False

    def get_success_url(self):
        return reverse('new_trip:trip_details', args=(self.object.trip_id,))# I get the foreign key id by adding _id to trip


class CatchDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Catch
    template_name = "catch_details/catch_confirm_delete.html"
    success_message = "Fogás törölve."

    # It limits that fishermen can only delete their own catches
    def test_func(self):
        catch = self.get_object()
        if self.request.user == catch.fisherman.user:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        # delete catch weight from the total_catch_weigt instance
        catch = self.get_object()
        current_trip = Trips.objects.get(trip_id=catch.trip_id)
        current_trip.total_catch_weight -= catch.weight
        current_trip.save()

        # success message for deleting catch
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('new_trip:trip_details', args=(self.object.trip_id,))
from django.shortcuts import render, redirect, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from new_trip.models import Fisherman, Trips, Catch, HookBait
#from .models import HookBait
from .forms import HookBaitForm, HookBaitFormset
from django.http import HttpResponse
from django.db.models import Sum
from django.views.generic.list import ListView


class ProfileView(DetailView):
    model = Fisherman
    template_name = "user_profile/profile.html"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # all related trips to the user
        context["all_trips"] = Trips.objects.filter(fisherman__user=self.request.user).count()

        # weight of all cathces
        """
        aggregation_weight = Catch.objects.filter(fisherman__user=self.request.user).aggregate(Sum('weight'))
        context["total_weight"] = aggregation_weight["weight__sum"]
        """
        # number of all catches
        context["all_catches"] = Catch.objects.filter(fisherman__user=self.request.user).count()

        # users's max catch
        context["max_catch"] = Catch.objects.filter(fisherman__user=self.request.user).order_by('-weight')[0:1]
        
        # List of own hookbaits
        context["own_hookbaits"] = HookBait.objects.filter(fisherman__user=self.request.user)

        return context 


class UserTripsView(ListView):
    model = Trips
    template_name = "user_profile/trips.html"
    context_object_name = "trips"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_trips"] = Trips.objects.filter(fisherman__user=self.request.user).order_by('-trip_id')
        return context


class UserCatchesView(ListView):
    model = Catch
    template_name = "user_profile/catches.html"
    context_object_name = "catches"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_catches"] = Catch.objects.filter(fisherman__user=self.request.user).order_by('-catch_id')
        return context


"""
class HookBaitCreateView(CreateView):
    model = HookBait
    template_name = "user_profile/hookbaits.html"
    form_class = HookBaitForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = HookBaitFormset(queryset=HookBait.objects.none())
        return context
    
    def post(self, request, *args, **kwargs):
        formset = HookBaitFormset(request.POST)
        if formset.is_valid():
            return self.form_valid(formset)

    def form_valid(self, formset):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.fisherman = self.request.user.fisherman
            instance.save()
        return super().form_valid(formset)

    def get_success_url(self):
        return reverse('trips_feed:feed')
"""

class HookBaitUpdateView(UpdateView):
    model = HookBait
    template_name = "user_profile/hookbaits.html"
    form_class = HookBaitForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = HookBaitFormset(queryset=HookBait.objects.filter(fisherman=self.request.user.fisherman))
        return context

    def post(self, request, *args, **kwargs):
        formset = HookBaitFormset(request.POST)
        if formset.is_valid():
            return self.form_valid(formset)
        else:
            return self.form_invalid(formset)

    def form_valid(self, formset):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.fisherman = self.request.user.fisherman
            instance.save()
        return super().form_valid(formset)

    def form_invalid(self, formset):
        return HttpResponse("Invalid")

    def get_success_url(self):
        return reverse('user_profile:profile', args=(self.kwargs['pk'],))

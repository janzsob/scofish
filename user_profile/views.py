from django.shortcuts import render, redirect, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from new_trip.models import Fisherman
from .models import HookBait
from .forms import HookBaitForm, HookBaitFormset
from django.http import HttpResponse


class ProfileView(DetailView):
    model = Fisherman
    template_name = "user_profile/profile.html"
    context_object_name = "profile"

"""
class HookBaitCreateView(CreateView):
    model = HookBait
    template_name = "user_profile/hookbait_create.html"
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


class HookBaitUpdateView(UpdateView):
    model = HookBait
    template_name = "user_profile/hookbait_create.html"
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
        return reverse('trips_feed:feed')
"""
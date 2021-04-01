from .models import Trips, Fisherman
from django.forms.formsets import formset_factory
from django import forms


class TripsForm(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ["place", "s_date", "e_date"]
        widgets = {
            "place": forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'lakeInput',}),
            "s_date": forms.DateTimeInput(format='%Y-%m-%d %H:%M', attrs={'class':'datetimefield form-control', 'id': 'StartingDate',}),
            "e_date": forms.DateTimeInput(format='%Y-%m-%d %H:%M', attrs={'class':'datetimefield form-control', 'id': 'EndingDate',}),
        }


class FishermanForm(forms.ModelForm):
    class Meta:
        model = Fisherman
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={'type': 'text', 'class': 'form-control my-1', 'id': 'FishermanInput',}),
        }

FishermanFormset = formset_factory(FishermanForm)
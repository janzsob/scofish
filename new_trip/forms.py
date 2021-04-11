from .models import Trips, Fisherman, Catch
from django.forms.formsets import formset_factory
from django import forms


class TripsForm(forms.ModelForm):
    class Meta:
        model = Trips
        fields = ["lake", "city", "s_date", "e_date"]
        widgets = {
            "lake": forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'LakeInput',}),
            "city": forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'CityInput',}),
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

class CatchForm(forms.ModelForm):
    fisherman = forms.ModelChoiceField(queryset= Fisherman.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    class Meta:
        model = Catch
        fields = ["fish_type", "weight", "length", "image", "datetime", "fisherman"]
        widgets = {
            "fish_type": forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            "weight": forms.NumberInput(attrs={'type': 'text', 'class': 'form-control', 'step': '0.01'}),
            "length": forms.NumberInput(attrs={'type': 'text', 'class': 'form-control'}),
            "datetime": forms.DateTimeInput(format='%Y-%m-%d %H:%M', attrs={'class':'datetimefield form-control'}),
        }

    def __init__(self, *args, **kwargs):
        fisherman = kwargs.pop('fisherman')
        super().__init__(*args, **kwargs)
        self.fields['fisherman'].queryset = fisherman
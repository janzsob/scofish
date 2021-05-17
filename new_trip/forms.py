from .models import Trips, Fisherman, Catch
from django import forms


class TripsForm(forms.ModelForm):
    fisherman = forms.ModelMultipleChoiceField(queryset=Fisherman.objects.all().exclude(user__username="admin"), widget=forms.SelectMultiple(attrs={'class': 'form-select'}))
    class Meta:
        model = Trips
        fields = ["lake", "city", "s_date", "e_date", "fisherman"]
        widgets = {
            "lake": forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'LakeInput',}),
            "city": forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'CityInput',}),
            "s_date": forms.DateTimeInput(format='%Y-%m-%d %H:%M', attrs={'class':'datetimefield form-control', 'id': 'StartingDate',}),
            "e_date": forms.DateTimeInput(format='%Y-%m-%d %H:%M', attrs={'class':'datetimefield form-control', 'id': 'EndingDate',}),
        }



class CatchForm(forms.ModelForm):
    fisherman = forms.ModelChoiceField(queryset= Fisherman.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    class Meta:
        model = Catch
        fields = ["fish_type", "weight", "length", "image", "datetime", "fisherman", "hook_bait","image"]
        widgets = {
            "fish_type": forms.Select(attrs={'class': 'form-select'}),
            "weight": forms.NumberInput(attrs={'type': 'text', 'class': 'form-control', 'step': '0.01'}),
            "length": forms.NumberInput(attrs={'type': 'text', 'class': 'form-control'}),
            "hook_bait": forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            "datetime": forms.DateTimeInput(format='%Y-%m-%d %H:%M', attrs={'class':'datetimefield form-control'}),
            "image": forms.FileInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        fisherman = kwargs.pop('fisherman')# it is the view def get_form_kwargs(self)
        super().__init__(*args, **kwargs)
        self.fields['fisherman'].queryset = fisherman
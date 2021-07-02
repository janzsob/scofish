from .models import Trips, Fisherman, Catch, HookBait
from django import forms
from django_select2 import forms as s2forms


class FishermanWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "user__username__istartswith",
    ]


class TripsForm(forms.ModelForm):
    fisherman = forms.ModelMultipleChoiceField(queryset=Fisherman.objects.all().exclude(user__username="admin"), widget=FishermanWidget(attrs={'class': 'form-select', 'data-language': 'hu'}))
    class Meta:
        model = Trips
        fields = ["lake", "city", "s_date", "e_date", "fisherman"]
        widgets = {
            "lake": forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'LakeInput',}),
            "city": forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'id': 'CityInput',}),
            "s_date": forms.DateTimeInput(format='%Y-%m-%d %H:%M', attrs={'class':'datetimefield form-control', 'id': 'StartingDate',}),
            "e_date": forms.DateTimeInput(format='%Y-%m-%d %H:%M', attrs={'class':'datetimefield form-control', 'id': 'EndingDate',}),
            #"fisherman": FishermanWidget(attrs = {'class': 'form-select'}),
        }



class CatchForm(forms.ModelForm):
    fisherman = forms.ModelChoiceField(queryset= Fisherman.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    #hookbait = forms.ModelChoiceField(queryset= HookBait.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}), required=False)
    class Meta:
        model = Catch
        fields = ["fish_type", "weight", "image", "datetime", "fisherman","image", "hookbait_name", "hookbait"]
        widgets = {
            "fish_type": forms.Select(attrs={'class': 'form-select'}),
            "weight": forms.NumberInput(attrs={'type': 'text', 'class': 'form-control', 'step': '0.01'}),
            #"length": forms.NumberInput(attrs={'type': 'text', 'class': 'form-control'}),
            "hookbait_name": forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
            "datetime": forms.DateTimeInput(format='%Y-%m-%d %H:%M', attrs={'class':'datetimefield form-control'}),
            "image": forms.FileInput(attrs={'class': 'form-control'}),
            "hookbait": forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        fisherman = kwargs.pop('fisherman')# it is the view def get_form_kwargs(self)
        super().__init__(*args, **kwargs)
        self.fields['fisherman'].queryset = fisherman

        # It needs to override the field because of the dependent select
        self.fields['hookbait'].queryset = HookBait.objects.none()

        # It needs for validation
        if 'fisherman' in self.data:
            try:
                fisherman_id = int(self.data.get('fisherman'))
                self.fields['hookbait'].queryset = HookBait.objects.filter(fisherman_id=fisherman_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Hookbait queryset
        # for updating the catch
        elif self.instance.pk:
            self.fields['hookbait'].queryset = self.instance.fisherman.hookbait_set.order_by('name')
        
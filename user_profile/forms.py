from django import forms
from .models import HookBait
from django.forms import modelformset_factory

class HookBaitForm(forms.ModelForm):

    class Meta:
        model = HookBait
        fields = ["name", "size", "taste"]
        widgets = {
            "name": forms.TextInput(attrs={'type': 'text', 'class': 'form-control', "placeholder": "Termék neve"}),
            "size": forms.TextInput(attrs={'type': 'text', 'class': 'form-control', "placeholder": "Méret"}),
            "taste": forms.TextInput(attrs={'type': 'text', 'class': 'form-control', "placeholder": "Íz"}),
        }
    

HookBaitFormset = modelformset_factory(HookBait, form=HookBaitForm, fields=["name", "size", "taste"], extra=1, can_delete=True)
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm): # Customizing UserCreationForm
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Felhasználónév...',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Email cím...',
        }
    ),
    #error_messages={'invalid': 'Adjon meg egy érvényes email címet.'}
    )
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control', 
            'placeholder': "Jelszó...",
        }
    ))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control', 
            'placeholder': "Jelszó megerősítése...",
        }
    ))
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    



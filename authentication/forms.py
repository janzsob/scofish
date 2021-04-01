from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm): # Customizing UserCreationForm
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Username...',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Email...',
        }
    ))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control', 
            'placeholder': "Enter password...",
        }
    ))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control', 
            'placeholder': "Confirm password...",
        }
    ))
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


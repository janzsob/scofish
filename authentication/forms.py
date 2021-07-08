from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class CreateUserForm(UserCreationForm): # Customizing UserCreationForm
    last_name = forms.CharField(max_length=70, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Vezetéknév', 
        }
    ))
    first_name = forms.CharField(max_length=70, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Keresztnév', 
        }
    ))
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Felhasználónév', 
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email', 
        }
    ),
    )
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Jelszó', 
        }
    ))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Jelszó megerősítése', 
        }
    ))
    
    class Meta:
        model = User
        fields = ["username", "last_name", "first_name", "email", "password1", "password2"]
    

# Add styling to password reset form in the template
class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
        'type': 'email',
        'name': 'email'
        }))


class PasswordResetConfrimForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetConfrimForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(
        label="Új jelszó",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control mb-2 mt-1',
            'type': 'password',
        }))

    new_password2 = forms.CharField(
        label="Új jelszó megerősítése",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control mb-2 mt-1',
            'type': 'password',
        }))
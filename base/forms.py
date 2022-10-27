from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
# from .models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password1'] 
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}), 
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'password1': forms.PasswordInput(attrs={'class': 'form-control'})}
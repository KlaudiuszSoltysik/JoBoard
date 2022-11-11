from django.forms import ModelForm
from django import forms
from .models import Offer


class OfferForm(ModelForm):
    class Meta:       
        model = Offer
        fields = ('industry', 'salary', 'city', 'company', 'description', 'email')
        
        widgets = {'industry': forms.Select(attrs={'type': 'text', 'name': 'industry', 'placeholder': 'Industry', 'class': 'form-control', 'autocomplete': 'off', 'style': 'margin-top: 0.4em; margin-bottom: 1em'}),
                  'salary': forms.NumberInput(attrs={'type': 'text', 'name': 'salary', 'placeholder': 'Salary', 'class': 'form-control', 'autocomplete': 'off', 'style': 'margin-top: 0.4em; margin-bottom: 1em'}),
                  'city': forms.TextInput(attrs={'type': 'text', 'name': 'city', 'placeholder': 'City', 'class': 'form-control', 'autocomplete': 'off', 'style': 'margin-top: 0.4em; margin-bottom: 1em'}),
                  'company': forms.TextInput(attrs={'type': 'text', 'name': 'company', 'placeholder': 'Company', 'class': 'form-control', 'autocomplete': 'off', 'style': 'margin-top: 0.4em; margin-bottom: 1em'}),
                  'description': forms.Textarea(attrs={'type': 'text', 'name': 'description', 'placeholder': 'Description', 'class': 'form-control', 'autocomplete': 'off', 'style': 'margin-top: 0.4em; margin-bottom: 1em'}),
                  'email': forms.EmailInput(attrs={'type': 'email', 'name': 'email', 'placeholder': 'Email address', 'class': 'form-control', 'autocomplete': 'off', 'style': 'margin-top: 0.4em; margin-bottom: 1em'})}
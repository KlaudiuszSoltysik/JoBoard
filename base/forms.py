from django import forms
from .models import MyUser

class MyUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = MyUser
        fields = ['email',
                  'first_name',
                  'last_name']
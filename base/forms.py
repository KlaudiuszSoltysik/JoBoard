# from django import forms
# from .models import MyUser, HR

# class MyUserForm(forms.ModelForm):
#     email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'autocomplete': 'off', 'style': 'margin-top: 0.4em; margin-bottom: 1em'}))
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name', 'autocomplete': 'off', 'style': 'margin-top: 0.4em; margin-bottom: 1em'}))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name', 'autocomplete': 'off', 'style': 'margin-top: 0.4em; margin-bottom: 1em'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'autocomplete': 'off', 'style': 'margin-top: 0.4em; margin-bottom: 1em'}))
    
#     class Meta:
#         model = MyUser
#         fields = ['email',
#                   'first_name',
#                   'last_name',
#                   'password']
        
# class HRForm(forms.ModelForm):
#     email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'autocomplete': 'off', 'style': 'margin-top: 0.4em; margin-bottom: 1em'}))
#     company = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company name', 'autocomplete': 'off', 'style': 'margin-top: 0.4em; margin-bottom: 1em'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'autocomplete': 'off', 'style': 'margin-top: 0.4em; margin-bottom: 1em'}))
    
#     class Meta:
#         model = HR
#         fields = ['email',
#                   'company',
#                   'password']
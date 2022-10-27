from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
import requests
import random


def home(request):
    response = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4e0ad1a0acb34407a06c85ae68a19813").json()['articles']
    random.shuffle(response)
    
    return render(request, 'home.html', {'response': response[0:5]})

def offers(request):   
    return render(request, 'offers.html')

def signUp(request):
    form = CreateUserForm()
    context = {'form': form}
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
    
    return render(request, 'sign-up.html', context)

def signIn(request):   
    return render(request, 'sign-in.html')

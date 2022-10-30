from django.shortcuts import render
from .forms import MyUserForm
import requests
import random


def home(request):
    try:
        response = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4e0ad1a0acb34407a06c85ae68a19813").json()['articles']
        random.shuffle(response)
    except:
        response = []
        
    return render(request, 'home.html', {'response': response[0:5]})

def offers(request):   
    return render(request, 'offers.html')

def signUp(request):
    form = MyUserForm()
    context = {'form': form}
    
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            form.save()
    
    return render(request, 'sign-up.html', context)

def signIn(request):   
    return render(request, 'sign-in.html')

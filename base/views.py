from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MyUserForm, HRForm
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

def signIn(request):    
    return render(request, 'sign-in.html')

def signUp(request):
    form = MyUserForm()
    context = {'form': form}
    
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Sign in to your new account.')
            return redirect('signIn')
        # else:
        #     messages.error(request, )
    
    return render(request, 'sign-up.html', context)

def signUpHR(request):
    form = HRForm()
    context = {'form': form}
    
    if request.method == 'POST':
        form = HRForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Sign in to your new account.')
            return redirect('signIn')
    
    return render(request, 'sign-up-hr.html', context)

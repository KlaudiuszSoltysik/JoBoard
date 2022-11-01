from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import MyUser, HR
import requests
import random


def home(request):    
    try:
        response = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4e0ad1a0acb34407a06c85ae68a19813").json()['articles']
        random.shuffle(response)
    except:
        response = []
        
    context = {'response': response[0:5],
               'users_count': MyUser.objects.count, 
               'companies_count': HR.objects.count}
        
    return render(request, 'home.html', context)

def offers(request):   
    return render(request, 'offers.html')

def signIn(request):    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, email)
            redirect('offers')
        else:
            messages.info(request, 'Email address or password is incorrect.')
    
    return render(request, 'sign-in.html')

def signUp(request):
    if request.method == 'POST':
        try:
            MyUser.objects.create_user(email=request.POST.get('email'), 
                                       first_name=request.POST.get('first_name'),   
                                       last_name=request.POST.get('last_name'), 
                                       password=request.POST.get('password'))   
                
            messages.success(request, 'Account created successfully. Sign in to your new account.')
            return redirect('signIn')
        
        except Exception as e:
            messages.warning(request, e)
        
    return render(request, 'sign-up.html')

def signUpHR(request):    
    if request.method == 'POST':
        try:
            HR.objects.create_user(email=request.POST.get('email'), 
                                   company=request.POST.get('company'),   
                                    password=request.POST.get('password'))   
                
            messages.success(request, 'Account created successfully. Sign in to your new account.')
            return redirect('signIn')
        
        except Exception as e:
            messages.warning(request, e)
    
    return render(request, 'sign-up-hr.html')

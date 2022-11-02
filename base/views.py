from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MyUser, HR
import requests
import random


user = None


def home(request):
    global user
    
    try:
        response = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4e0ad1a0acb34407a06c85ae68a19813").json()['articles']
        random.shuffle(response)
    except:
        response = []
        
    context = {'user': user,
               'response': response[0:5],
               'users_count': MyUser.objects.count,
               'companies_count': HR.objects.count}
        
    return render(request, 'home.html', context)

def offers(request):
    global user
    
    context = {'user': user}
    
    return render(request, 'offers.html', context)

def signIn(request):
    global user
      
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = MyUser.objects.get(email=email)
        except MyUser.DoesNotExist:
            try:
                user = HR.objects.get(email=email)
            except HR.DoesNotExist:
                user = None
        
        if user is not None:
            if user.check_password(password):
                return redirect('offers')
            else:
                messages.warning(request, 'Password is incorrect. Try again or reset password.')
        else:
            messages.warning(request, 'Email address is not signed up. Try again or sign up.')
    
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

def accessDennied(request):
    return render(request, 'access-dennied.html')
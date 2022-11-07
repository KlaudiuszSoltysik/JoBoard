from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MyUser, HR, Offer
from .forms import OfferForm
import requests
import random


user = None
is_logged = False


def home(request):
    global is_logged
    
    try:
        response = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4e0ad1a0acb34407a06c85ae68a19813").json()['articles']
        random.shuffle(response)
    except:
        response = []
        
    context = {'is_logged': is_logged,
               'response': response[0:5],
               'users_count': MyUser.objects.count,
               'offers_count': Offer.objects.count,
               'companies_count': HR.objects.count}
        
    return render(request, 'home.html', context)


def offers(request):
    global is_logged
    
    context = {'is_logged': is_logged}
    
    return render(request, 'offers.html', context)


def signIn(request):
    global user
    global is_logged
    
    context = {'is_logged': is_logged}
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = MyUser.objects.get(email=email)
        except MyUser.DoesNotExist:
            user = None
        
        if user is not None:
            if user.check_password(password):
                is_logged = True
                
                if request.POST.get('remember'):
                    request.session.set_expiry(1209600)
                    
                messages.success(request, 'Signed in.')
                return redirect('offers')
            else:
                messages.warning(request, 'Password is incorrect. Try again or reset password.')
        else:
            messages.warning(request, 'Email address is not signed up. Try again or sign up.')
    
    return render(request, 'sign-in.html', context)


def signInHR(request):
    global user
    global is_logged
    
    context = {'is_logged': is_logged}
      
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = HR.objects.get(email=email)
        except HR.DoesNotExist:
            user = None
        
        if user is not None:
            if user.check_password(password):
                is_logged = True
                
                if request.POST.get('remember'):
                    request.session.set_expiry(1209600)
                    
                messages.success(request, 'Signed in.')
                return redirect('offers')
            else:
                messages.warning(request, 'Password is incorrect. Try again or reset password.')
        else:
            messages.warning(request, 'Email address is not signed up. Try again or sign up.')
    
    return render(request, 'sign-in-hr.html', context)


def signUp(request):
    global is_logged
    
    context = {'is_logged': is_logged}
    
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
        
    return render(request, 'sign-up.html', context)


def signUpHR(request):
    global is_logged
    
    context = {'is_logged': is_logged}
    
    if request.method == 'POST':
        try:
            HR.objects.create_user(email=request.POST.get('email'), 
                                   company=request.POST.get('company'),   
                                   password=request.POST.get('password'))   
                
            messages.success(request, 'Account created successfully. Sign in to your new account.')
            return redirect('signIn')
        
        except Exception as e:
            messages.warning(request, e)
    
    return render(request, 'sign-up-hr.html', context)


def manageAccount(request):
    global user
    global is_logged
    
    context = {'user': user,
               'is_logged': is_logged}
    
    if user is None:
        return redirect('accessDennied')
    else:
        pass
    
    return render(request, 'manage-account.html', context)


def addOffer(request):
    global user
    global is_logged
    
    context = {'form': OfferForm(),
               'user': user,
               'is_logged': is_logged}
    
    if user is None:
        return redirect('accessDennied')
    else:
        if request.method == 'POST':
            
            form = OfferForm(request.POST)
            
            if form.is_valid():
                messages.success(request, 'Offer added.')
                return redirect('offers')
            else:
                messages.warning(request, 'Something went wrong.')
    
    return render(request, 'add-offer.html', context)


def signOut(request):
    global user
    global is_logged
    user = None
    is_logged = False
    
    return redirect('home')


def accessDennied(request):
    return render(request, 'access-dennied.html')
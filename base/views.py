from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail

from .models import MyUser, HR, Offer
from .forms import OfferForm, MyUserPasswordResetForm

import requests
import random
import re

# google login
# fb login
# filtry
# edycja konta, ogłoszeń

user = None
is_logged = False


def home(request):
    global is_logged
    global user
    
    try:
        response = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4e0ad1a0acb34407a06c85ae68a19813").json()['articles']
        random.shuffle(response)
    except:
        response = []
        
    context = {'is_logged': is_logged,
               'user': user,
               'response': response[0:5],
               'users_count': MyUser.objects.count,
               'offers_count': Offer.objects.count,
               'companies_count': HR.objects.count}
        
    return render(request, 'home.html', context)


def offers(request):
    global is_logged
    global user
    
    paginator = Paginator(Offer.objects.all(), 1)
    page = request.GET.get('page')
    offers = paginator.get_page(page)
    
    if offers.paginator.num_pages < 5:
        page_numbers = range(1, offers.paginator.num_pages + 1)
    else:
        if offers.number < 3:
            min = 1
        else:
            min = offers.number - 2
        if offers.number > offers.paginator.num_pages - 2:
            max = offers.paginator.num_pages + 1
        else:
            max = offers.number + 3
            
        page_numbers = list(range(min, max))
        page_numbers.append('...')
        page_numbers.append(offers.paginator.num_pages)
    
    context = {'is_logged': is_logged,
               'user': user,
               'offers': offers,
               'page_numbers': page_numbers}
    
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
    global is_logged
    global user
    
    context = {'is_logged': is_logged,
               'user': user}
    
    if user is None:
        return redirect('accessDennied')
    else:
        pass
    
    return render(request, 'manage-account.html', context)


def addOffer(request):
    global is_logged
    global user
    
    context = {'form': OfferForm(),
               'is_logged': is_logged,
               'user': user}
    
    if user is None:
        return redirect('accessDennied')
    else:
        if request.method == 'POST':
            
            form = OfferForm(request.POST)
            
            if len(re.findall('\d+', request.POST.get('salary'))) != 1:
                messages.warning(request, 'Salary field error.')
                
            elif form.is_valid():                
                Offer.objects.create(position=request.POST.get('position'),
                                     industry=request.POST.get('industry'),
                                     salary=request.POST.get('salary'),
                                     city=request.POST.get('city') if request.POST.get('city') else 'Remote',
                                     company=request.POST.get('company'),
                                     description=request.POST.get('description'),
                                     email=request.POST.get('email'),
                                     author=user)
                
                messages.success(request, 'Offer added.')
                return redirect('offers')
            else:
                messages.warning(request, 'Something went wrong.')
    
    return render(request, 'add-offer.html', context)


def signOut(request):
    global is_logged
    global user
    is_logged = False
    user = None
    
    return redirect('home')


def passwordReset(request):    
    if request.method == "POST":
        password_reset_form = MyUserPasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            user = MyUser.objects.get(email=password_reset_form.cleaned_data['email'])
            if user:
                subject = "Password Reset Requested"
                email_template_name = "../templates/registration/password_reset_email.txt"
                c = {'email': user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'JoBoard',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'user': user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http'}
                email = render_to_string(email_template_name, c)
                try:
                    send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    messages.success(request, f'Email sent. Check your {user.email} inbox.')
                except:
                    messages.warning(request, 'Something went wrong.')
            else:
                messages.warning(request, f'User {user.email} does not exist.')
            return redirect ("/password_reset/done/")
     
    password_reset_form = MyUserPasswordResetForm()
    return render(request, '../templates/registration/password_reset.html', context={'password_reset_form': password_reset_form})


def accessDennied(request):
    return render(request, 'access-dennied.html')
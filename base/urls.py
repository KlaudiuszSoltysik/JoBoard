from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('offers/', views.offers, name='offers'),
    path('sign-in/', views.signIn, name='signIn'),
    path('sign-up/', views.signUp, name='signUp'),
    path('sign-up-hr/', views.signUpHR, name='signUpHR'),
    path('access-dennied/', views.accessDennied, name='accessDennied')
]
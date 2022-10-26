from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-up/', views.signUp, name='signUp'),
    path('sign-in/', views.signIn, name='signIn'),
]
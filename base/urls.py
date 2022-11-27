from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('offers/', views.offers, name='offers'),
    path('sign-in/', views.signIn, name='signIn'),
    path('sign-in-hr/', views.signInHR, name='signInHR'),
    path('sign-up/', views.signUp, name='signUp'),
    path('sign-up-hr/', views.signUpHR, name='signUpHR'),
    path('sign-up-hr/', views.signUpHR, name='signUpHR'),
    path('manage-account/', views.manageAccount, name='manageAccount'),
    path('add-offer/', views.addOffer, name='addOffer'),
    path('edit-offer/<str:pk>/', views.editOffer, name='editOffer'),
    path('offer/<str:pk>/', views.offer, name='offer'),
    path('sign-out/', views.signOut, name='signOut'),
    path('password-reset/', views.passwordReset, name='passwordReset'),
    path('access-dennied/', views.accessDennied, name='accessDennied')
]
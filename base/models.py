from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import MyUserAccountManager, HRAccountManager


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email address', unique=True, max_length=30)
    first_name = models.CharField('First name', max_length=30)
    last_name = models.CharField('Last name', max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = MyUserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    
    
class HR(AbstractBaseUser):
    email = models.EmailField('Email address', unique=True)
    company = models.CharField('Company name', max_length=50)
    description = models.CharField('Company description', max_length=500)
    url = models.CharField('Company URL', max_length=100)

    objects = HRAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['company']

    def __str__(self):
        return self.email
    
    
class Offer(models.Model):
    INDUSTRY_CHOICES = (('IT','IT'),
                        ('Marketing', 'MARKETING'),
                        ('Construction','CONSTRUCTION'),
                        ('Engineering','ENGINEERING'),
                        ('Education','EDUCATION'),
                        ('Finance', 'FINANCE'),
                        ('Health care', 'HEALTH_CARE'),
                        ('Media', 'MEDIA'))
    
    industry = models.CharField('Industry field', max_length=12, choices=INDUSTRY_CHOICES, default='Education')
    salary = models.IntegerField('Salary', blank=True, null=True)
    city = models.CharField('City', max_length=30, blank=True, null=True)
    company = models.CharField('Company name', max_length=50)
    description = models.CharField('Description', max_length=1000)
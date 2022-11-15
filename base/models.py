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
    INDUSTRY_CHOICES = (('Other', 'Other'),
                        ('Agriculture', 'Agriculture'),
                        ('Construction','Construction'),
                        ('Education','Education'),
                        ('Energy', 'Energy'),
                        ('Engineering','Engineering'),
                        ('Entertainment', 'Entertainment'),
                        ('Fashion', 'Fashion'),
                        ('Finance', 'Finance'),
                        ('Food', 'Food'),
                        ('Health care', 'Health care'),
                        ('IT','IT'),
                        ('Manufacturing', 'Manufacturing'),
                        ('Marketing', 'Marketing'),
                        ('Media', 'Media'))
    
    position = models.CharField('Job position', max_length=70)
    industry = models.CharField('Industry field', max_length=13, choices=INDUSTRY_CHOICES, default='Other')
    salary = models.IntegerField('Salary', blank=True, null=True)
    city = models.CharField('City', max_length=30, blank=True, null=True)
    company = models.CharField('Company name', max_length=50)
    description = models.CharField('Description', max_length=5000)
    email = models.EmailField('Email address',  max_length=30)
    author = models.ForeignKey(HR, on_delete=models.CASCADE)

    def __str__(self):
            return self.email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class MyUserAccountManager(BaseUserManager):
    def create_superuser(self, email, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, first_name, last_name, password, **other_fields)

    def create_user(self, email, first_name, last_name, password, **other_fields):
        if not email or not first_name or not last_name or not password:
            raise ValueError('You must provide more data.')
        elif len(password)<8:
            raise ValueError('Password too short.')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        
        return user
    

class HRAccountManager(BaseUserManager):
    def create_user(self, email, company, password, **other_fields):
        if not email or not company or not password:
            raise ValueError('You must provide more data')
        elif len(password)<8:
            raise ValueError('Password too short.')

        email = self.normalize_email(email)
        user = self.model(email=email, company=company, **other_fields)
        user.set_password(password)
        user.save()    
            
        return user


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
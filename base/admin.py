from django.contrib import admin
from .models import MyUser, HR, Offer

admin.site.register(MyUser)
admin.site.register(HR)
admin.site.register(Offer)
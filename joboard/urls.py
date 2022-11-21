from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from base.forms import MyUserSetPasswordForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html', form_class=MyUserSetPasswordForm), name='password_reset_confirm'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),  
]
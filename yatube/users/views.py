from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

from .forms import CreationForm

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'

class PasswordChange(PasswordChangeView):
    form_class = CreationForm
    success_url = reverse_lazy('password_change/done/')
    template_name = 'users/password_change_form.html'

class Logout(LogoutView):
    template_name = 'users/logged_out.html'
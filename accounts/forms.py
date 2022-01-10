from django import forms
from django.db import models
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField()
    confirm_password = forms.CharField()
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']



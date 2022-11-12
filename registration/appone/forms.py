from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm

from .models import Address


from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class AddressRegistrationForm(ModelForm):
    class Meta:
        model = Address
        fields = ['address_1','address_2','state','city']
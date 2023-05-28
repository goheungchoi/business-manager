# app/forms.py
from django import forms
from .models import User, Account, Address

class UserLoginForm(forms.Form):
  username = forms.CharField(max_length=40)
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserSignupForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

  class Meta:
    model = User
    fields = ['name', 'username', 'department', 'title', 'role', 'email', 'email_signature', 'phone', 'mobile', 'home_phone', 'manager']

class AccountUpdateForm(forms.ModelForm):
  class Meta:
    model = Account
    fields = ['name', 'phone', 'active', 'type']  # and other fields you need

class AddressUpdateForm(forms.ModelForm):
  class Meta:
    model = Address
    fields = ['street', 'city', 'state', 'zip_code', 'country']
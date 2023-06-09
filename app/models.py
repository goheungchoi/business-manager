# app/models.py
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")

class Address(models.Model):
  street = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=255)
  zip_code = models.CharField(max_length=10)
  country = models.CharField(max_length=255)

class User(AbstractBaseUser):
  ROLE_CHOICES = [
    ('MANAGER', 'Manager'),
    ('EMPLOYEE', 'Employee'),
    ('ADMIN', 'Admin'),
    ('OTHER', 'Other'),
  ]
  first_name = models.CharField(max_length=150, default='')
  last_name = models.CharField(max_length=150, default='')
  username = models.CharField(max_length=80, unique=True)
  department = models.CharField(max_length=80)
  title = models.CharField(max_length=80)
  role = models.CharField(choices=ROLE_CHOICES, max_length=20, default='OTHER')
  email = models.EmailField()
  email_signature = models.TextField(max_length=1333)
  phone = models.CharField(max_length=16, validators=[phone_validator])
  mobile = models.CharField(max_length=16, validators=[phone_validator])
  home_phone = models.CharField(max_length=16, validators=[phone_validator])
  manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
  password_reset_attempt = models.PositiveSmallIntegerField(default=0)
  password_reset_lockout_date = models.DateTimeField(null=True, blank=True)
  USERNAME_FIELD = "username"
  EMAIL_FIELD = "email"
  REQUIRED_FIELDS = ["first_name", 
                     "last_name", 
                     "username", 
                     "email", 
                     "phone"]

class Account(models.Model):
  ACCOUNT_TYPE_CHOICES = [
    ('PROSPECT', 'Prospect'),
    ('PENDING', 'Pending'),
    ('CUSTOMER', 'Customer'),
    ('OTHER', 'Other'),
  ]
  first_name = models.CharField(max_length=150, default='')
  last_name = models.CharField(max_length=150, default='')
  billing_address = models.ForeignKey(Address, on_delete=models.CASCADE)
  phone = models.CharField(max_length=15, default='')
  is_active = models.BooleanField(default=True)
  type = models.CharField(max_length=15, choices=ACCOUNT_TYPE_CHOICES, default='OTHER')

class Contact(models.Model):
  account = models.ForeignKey(Account, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=150, default='')
  last_name = models.CharField(max_length=150, default='')
  birthdate = models.DateField()
  email = models.EmailField()
  email_opt_out = models.BooleanField(default=False)
  home_phone = models.CharField(max_length=15, default='')
  mailing_address = models.ForeignKey(Address, on_delete=models.CASCADE)
  mobile = models.CharField(max_length=15, default='')
  
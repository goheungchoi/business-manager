# app/admin.py
from django.contrib import admin
from .models import User, Account, Address, Contact

class UserAdmin(admin.ModelAdmin):
  list_display = ('name', 'username', 'email', 'department', 'role')
  search_fields = ('name', 'username', 'email', 'department', 'role')

class AccountAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'phone', 'type')
  search_fields = ('id', 'name', 'phone', 'type')

class AddressAdmin(admin.ModelAdmin):
  list_display = ('street', 'city', 'state', 'zip_code', 'country')
  search_fields = ('street', 'city', 'state', 'zip_code', 'country')

class ContactAdmin(admin.ModelAdmin):
  list_display = ('account', 'birthdate', 'email', 'name')
  search_fields = ('account', 'birthdate', 'email', 'name')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Contact, ContactAdmin)

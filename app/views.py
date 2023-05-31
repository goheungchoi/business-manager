# app/views.py
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserSignupForm, AccountUpdateForm, AddressUpdateForm
from .models import User, Account, Address
from django.views import View
from django.contrib import messages

User = get_user_model()

def index(request):
    context = {}
    return render(request, "index.html", context)

class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'business-manager/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                messages.success(request, 'Please check your email to verify your login.', 'success')
            else:
                messages.error(request, 'Your username or password is incorrect.', 'danger')
        return render(request, self.template_name, {'form': form})

def email_verification(request, token):
    auth_token = request.session.get('auth_token')
    auth_user_id = request.session.get('auth_user_id')
    if auth_token == token and auth_user_id is not None:
        # The token is correct and we have a user ID, let's log the user in
        User = get_user_model()
        user = User.objects.get(pk=auth_user_id)
        login(request, user)
        messages.success(request, 'Verification Succeeded', 'success')
        return redirect('core:home')
    else:
        # The token was incorrect or we don't have a user ID, show an error page
        messages.error(request, 'Verification failed', 'danger')
        return redirect('core:login')

class UserSignupView(View):
    form_class = UserSignupForm
    template_name = 'business-manager/signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'You have successfully signed up.', 'success')
            return redirect('core:home')
        return render(request, self.template_name, {'form': form})

class AccountUpdateView(View):
    account_form_class = AccountUpdateForm
    address_form_class = AddressUpdateForm
    template_name = 'business-manager/update_account.html'

    def get(self, request, id):
        account = Account.objects.get(pk=id)
        account_form = self.account_form_class(instance=account)
        address_form = self.address_form_class(instance=account.billing_address)
        return render(request, self.template_name, {'account_form': account_form, 'address_form': address_form})

    def post(self, request, id):
        account = Account.objects.get(pk=id)
        account_form = self.account_form_class(request.POST, instance=account)
        address_form = self.address_form_class(request.POST, instance=account.billing_address)
        if account_form.is_valid() and address_form.is_valid():
            account_form.save()
            address_form.save()
            messages.success(request, 'Your account information has been updated.', 'success')
            return redirect('core:home')
        return render(request, self.template_name, {'account_form': account_form, 'address_form': address_form})
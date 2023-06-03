# app/views.py
# this is for traditional django templates
# therefore, this views are not compatible with React UI
from django.http import JsonResponse
from .crypto import decode_token
from django.conf import settings
from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserSignupForm, AccountUpdateForm, AddressUpdateForm
from .models import User, Account, Address
from django.views import View
from django.contrib import messages

from rest_framework_simplejwt.tokens import RefreshToken


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
    try:
        payload = decode_token(token, settings.SECRET_KEY)
        user_id = payload['user_id']
    except:
        return JsonResponse({'status': 'error', 'message': 'Invalid or expired token.'}, status=400)
    
    # The token is correct and we have a user ID
    User = get_user_model()
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({
            'status': 'error', 
            'message': 'Invalid user ID'}, status=400)

    refresh = RefreshToken.for_user(user)
    login(request, user)
    return JsonResponse({
        'status': 'success', 
        'message': 'Verification Succeeded', 
        'access' : str(refresh.access_token),
        'refresh': str(refresh)}, status=200)

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
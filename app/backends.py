# app/backends.py
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.urls import reverse
from uuid import uuid4
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import check_password
from django.http.request import HttpRequest

class EmailVerificationBackend(ModelBackend):
  def authenticate(self, request: HttpRequest, username=None, password=None, **kwargs):
    User = get_user_model()
    try:
      user = User.objects.get(username=username)
      if user and user.check_password(password):
        # User credentials are correct, now we generate and store the token
        token = uuid4()
        request.session['auth_token'] = str(token)
        request.session['auth_user_id'] = user.pk

        # Send the token to the user's email
        verification_url = request.build_absolute_uri(reverse('email_verification', args=[token]))
        send_mail(
            'Verify your login',
            f'Click the link to log in: {verification_url}',
            'from@example.com',
            [user.email],
        )

        return None 
      else:
        return None
    except User.DoesNotExist:
      return None
            
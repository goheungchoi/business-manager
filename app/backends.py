# app/backends.py
from .models import User
from .crypto import create_token
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from uuid import uuid4
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import check_password
from django.http.request import HttpRequest

from django.conf import settings

class EmailVerificationBackend(ModelBackend):
  def authenticate(self, request: HttpRequest, username=None, password=None, **kwargs):
    print("backend auth method is passed")
    #User = get_user_model()
    try:
      user = User.objects.get(username=username)
      if user and check_password(password, user.password):
        # User credentials are correct, now we generate and store the token
        token = create_token(user.pk, settings.SECRET_KEY)

        # Send the token to the user's email
        print(f'start sending an email')
        #verification_url = request.build_absolute_uri(reverse('email_verification', args=[token]))
        verification_url = f"http://localhost:3000/email_verification/{token}"
        send_mail(
            subject='Verify your login',
            message=f'Click the link to log in: {verification_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        print('email sent')

        return user
      else:
        return None
    except User.DoesNotExist:
      return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None
            
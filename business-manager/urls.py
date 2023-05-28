# business-manager/urls.py
from django.urls import path
from app.views import UserLoginView, UserSignupView, AccountUpdateView, email_verification

urlpatterns = [
  path('login/', UserLoginView.as_view(), name='login'),
  path('signup/', UserSignupView.as_view(), name='signup'),
  path('update_account/<int:id>/', AccountUpdateView.as_view(), name='update_account'),
  path('email_verification/<uuid:token>/', email_verification, name='email_verification'),
]
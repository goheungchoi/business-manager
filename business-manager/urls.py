# business-manager/urls.py
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from app.views import index, UserLoginView, UserSignupView, AccountUpdateView, email_verification
from graphene_django.views import GraphQLView
from app.schema import schema
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'business-manager'

urlpatterns = [
  path('django-admin/', admin.site.urls),
  path('api/graphql', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
  path('', index, name='index'),
  path('api/login/', UserLoginView.as_view(), name='login'),
  path('api/signup/', UserSignupView.as_view(), name='signup'),
  path('api/update_account/<int:id>/', AccountUpdateView.as_view(), name='update_account'),
  path('api/email_verification/<uuid:token>/', email_verification, name='email_verification'),
  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

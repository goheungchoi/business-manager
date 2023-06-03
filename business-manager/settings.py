# business-manager/settings.py
import os
import environ  # hide credential info

env = environ.Env()
environ.Env.read_env()

DEBUG = True

INSTALLED_APPS = [
  "django.contrib.admin",
  "django.contrib.auth",
  "django.contrib.contenttypes",
  "django.contrib.sessions",
  "django.contrib.messages",
  "django.contrib.staticfiles",
  
  "app.apps.AppConfig",

  "graphene_django",
  "corsheaders",
  'rest_framework_simplejwt',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'postgres',
    'USER': 'postgres',
    'PASSWORD': 'my_db_password',
    'HOST': 'localhost',
    'PORT': '5432', 
  }
}

# SMTP settings (Email Sending Protocol)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')


GRAPHENE = {
  'SCHEMA': 'app.schema.schema', 
}

MIDDLEWARE = [
  "django.middleware.security.SecurityMiddleware",
  'corsheaders.middleware.CorsMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
  "django.contrib.sessions.middleware.SessionMiddleware",
  "django.middleware.common.CommonMiddleware",
  "django.middleware.csrf.CsrfViewMiddleware",
  "django.contrib.auth.middleware.AuthenticationMiddleware",
  "django.contrib.messages.middleware.MessageMiddleware",
  "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'client', 'build'),
                    os.path.join(BASE_DIR, 'client', 'build', 'static')]

TEMPLATES = [
  {
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [os.path.join(BASE_DIR, 'templates', 'business-manager')],
    "APP_DIRS": True,
    "OPTIONS": {
      "context_processors": [
        "django.template.context_processors.debug",
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
      ],
    },
  },
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
CORS_ALLOW_HEADERS = [
    "withcredentials",
]

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
ROOT_URLCONF = "business-manager.urls"
AUTHENTICATION_BACKENDS = ["app.backends.EmailVerificationBackend"]

SECRET_KEY = 'a3jg7sdjkgf7^&sdjhg8237sd87f6sdf^&sdf7s6d8f7sdf^&'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



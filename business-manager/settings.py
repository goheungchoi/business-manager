# business-manager/settings.py

INSTALLED_APPS = [
  "django.contrib.admin",
  "django.contrib.auth",
  "django.contrib.contenttypes",
  "django.contrib.sessions",
  "django.contrib.messages",
  "django.contrib.staticfiles",
  
  "app.apps.AppConfig",

  "graphene_django"
]

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

GRAPHENE = {
  'SCHEMA': 'app.schema.schema', 
}

MIDDLEWARE = [
  "django.middleware.security.SecurityMiddleware",
  "django.contrib.sessions.middleware.SessionMiddleware",
  "django.middleware.common.CommonMiddleware",
  "django.middleware.csrf.CsrfViewMiddleware",
  "django.contrib.auth.middleware.AuthenticationMiddleware",
  "django.contrib.messages.middleware.MessageMiddleware",
  "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
  {
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [],
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

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
ROOT_URLCONF = "business-manager.urls"
AUTHENTICATION_BACKENDS = ["business-manager.backends.EmailVerificationBackend"]

SECRET_KEY = 'a3jg7sdjkgf7^&sdjhg8237sd87f6sdf^&sdf7s6d8f7sdf^&'

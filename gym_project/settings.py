"""
@authors Alexander Fisher & Jonathan Salem
@version Barbell Version 1.2

@about This settings file configures the Django project 'Barbell', defining its behavior in various environments. 

        *Environment and Directory Configuration:
            - BASE_DIR defines the root directory of the project for relative path configurations.
            - ENV_PATH handles the optional loading of environment variables from a '.env' file for secret management.

        *Development and Production Settings:
            - SECRET_KEY is the key used for cryptographic signing, fetched from environment variables for security.
            - DEBUG flag toggles the debug mode, affecting error reporting and static file serving.  "DEBUG = True" -> for in-browser debug info
            - ALLOWED_HOSTS defines which hosts/domains the app can serve.

        *Application Registration:
            - INSTALLED_APPS lists Django and third-party apps used in the project, enabling their functionalities.

        *Logging Configuration:
            - LOGGING defines the logging configuration to output debug information to the console.

        *Middleware Configuration:
            - MIDDLEWARE lists the middleware components that are processed during request/response lifecycle.

        *Template Engine Configuration:
            - TEMPLATES configures Django's template engine, including directories to search for HTML template files.

        *WSGI Configuration:
            - WSGI_APPLICATION points to the WSGI application used by Django's development server or a WSGI server.

        *Database Configuration:
            - DATABASES defines the settings for connecting to the project's database, including credentials and host.

        *Authentication and Authorization:
            - AUTH_PASSWORD_VALIDATORS configures validators for user passwords to enforce security requirements.
            - AUTH_USER_MODEL overrides the default user model with a custom model for extended functionalities.

        *Internationalization and Localization:
            - LANGUAGE_CODE sets the language for the project.
            - TIME_ZONE configures the timezone.
            - USE_I18N and USE_TZ enable Django's internationalization and timezone support.

        *Static and Media Files:
            - STATIC_URL and STATICFILES_DIRS configure the serving of static files.
            - DEFAULT_FILE_STORAGE and GS_BUCKET_NAME configure Google Cloud Storage for media file handling.

        *Email Configuration:
            - EMAIL_BACKEND and related settings configure email sending capabilities, using SendGrid in this case.

        *Site Configuration:
            - SITE_ID specifies the current site's ID for use with Django's "sites" framework.

        *Security and Sessions:
            - Various settings to enforce HTTPS and secure cookies, plus configuration for CSRF protection.

        *Custom User Model and Authentication Backend:
            - Specifies a custom user model and additional authentication backend for use with django-allauth.

        *Social Authentication and Email Verification:
            - Configuration for handling social authentication and email verification processes.
"""

from pathlib import Path
from decouple import config
from django.conf import settings
from google.oauth2 import service_account
import os

""" 
------*Environment and Directory Configuration 
"""
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = os.path.join(BASE_DIR, 'ENV', 'secret.env')
if os.path.exists(ENV_PATH):
    with open(ENV_PATH) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                os.environ[key] = value


"""
------*Development and Production Settings
"""
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Change for production
DEBUG = True
ALLOWED_HOSTS = ['164.90.134.67', 'socialbarbell.com', 'www.socialbarbell.com', '127.0.0.1']

"""
------*Application Registration
"""
# Application definition
INSTALLED_APPS = [
    'storages',
    'gym_app.apps.GymAppConfig',
    'allauth',
    'allauth.account',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

"""
------*Logging Configuration
"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/error.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

"""
------*Middleware Configuration
"""
MIDDLEWARE = [
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gym_project.urls'

"""
------*Template Engine Configuration
"""
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'gym_app', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

""" 
------*WSGI Configuration
"""
WSGI_APPLICATION = 'gym_project.wsgi.application'

"""
------*Database Configuration
""" 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'accounts_db',
        'USER': 'barbell_midir',
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': 'localhost',  # Change if your MySQL server is running on a different host
        'PORT': '3306',       # Default MySQL port
    }
}

"""
------*Authentication and Authorization
"""

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

"""
------*Internationalization and Localization
"""

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


"""
------*Static and Media Files
"""

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


AUTH_USER_MODEL = 'gym_app.CustomUser'

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.path.join(BASE_DIR, 'GCS', 'elegant-azimuth-399823-2926231d859f.json')
)
GS_BUCKET_NAME = 'barbell_bucket_1'

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
MEDIA_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/'

GS_FILE_OVERWRITE = False
MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_BUCKET_NAME)

"""
------*Email Configuration
"""

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# -----set up for sending emails
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = config('SENDGRID_API_KEY')
DEFAULT_FROM_EMAIL = 'barbellauth@socialbarbell.com'

# *Site Configuration
# The sites domain and name for constructing the reset link
SITE_ID = 1
LOGIN_REDIRECT_URL = 'profile_self'

"""
------*Security and Sessions
"""
if DEBUG:
    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_DOMAIN = None


else:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_DOMAIN = ['https://www.socialbarbell.com', 'https://socialbarbell.com', '.127.0.0.1']
   
   
CSRF_TRUSTED_ORIGINS = ['https://socialbarbell.com']
if DEBUG:
    CSRF_TRUSTED_ORIGINS.append('https://127.0.0.1')


"""
------*Custom User Model and Authentication Backend
"""
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
 
AUTH_USER_MODEL = 'gym_app.CustomUser'

"""
------*Social Authentication and Email Verification
"""
#ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/signin/'
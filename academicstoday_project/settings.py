"""
Django settings for academicstoday_project project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

# Import variables for our application. Basically all imported variables
# have a SECRET_* prefix.

try:
    from academicstoday_project.secret_settings_example import *
except ImportError:
    pass

# Import all constants to use throughout our application
try:
    from academicstoday_project.constants import *
except ImportError:
    pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = SECRET_DEBUG

ALLOWED_HOSTS = SECRET_ALLOWED_HOSTS

# 'Sites Framework' requires this line.
SITE_ID = 1


# Application definition
#

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    #'captcha',
    'account',
    'landpage',
    'registration',
    'login',
    'registrar',
    'student',
    'teacher'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'academicstoday_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'academicstoday_project.wsgi.application'



# Captcha App
#
if 'test' in sys.argv:
    CAPTCHA_TEST_MODE = True
CAPTCHA_FONT_SIZE = 52



# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, 'db.sqlite3'),
        "USER": SECRET_DB_USER,
        "PASSWORD": SECRET_DB_PASSWORD,
        "HOST": "localhost",
        "PORT": "5432",
    }
}



# Email
# http://stackoverflow.com/questions/19264907/python-django-gmail-smtp-setup

EMAIL_USE_TLS = True
EMAIL_HOST = SECRET_EMAIL_HOST
EMAIL_PORT = SECRET_EMAIL_PORT
EMAIL_HOST_USER = SECRET_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = SECRET_EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
DEFAULT_TO_EMAIL = EMAIL_HOST_USER



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Toronto'

USE_I18N = True

USE_L10N = True

USE_TZ = False



# Static files (CSS, JavaScript, Images) & Upload Content
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "media"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
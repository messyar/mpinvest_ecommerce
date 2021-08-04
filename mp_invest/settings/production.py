import os
from mp_invest.settings.base import *

ALLOWED_HOSTS = ['mp-invest.ru']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'postgres.c35040.h2',
        'PORT': '5432',
        'NAME': 'c35040_mp_invest_ru',
        'USER': 'c35040_mp_invest_ru',
        'PASSWORD': 'BuLqaPifbigis78',
    },
}

WSGI_APPLICATION = 'mp_invest.wsgi.application'

STATIC_URL = '/static/'
STATIC_ROOT = '/home/c35040/mp-invest.ru/www/static'

STATICFILES_DIRS = [
    '/home/c35040/mp-invest.ru/www/static',
    os.path.join(BASE_DIR, "www/static"),

]

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/c35040/mp-invest.ru/www/media'

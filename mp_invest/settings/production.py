import os
from mpi_shop.settings.base import *

ALLOWED_HOSTS = ['192.162.64.87']

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

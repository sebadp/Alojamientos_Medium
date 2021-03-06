from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['saracura2.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dah5hinhc1fr92',
        'USER':'pdjdsilreeaovy',
        'PASSWORD': '9d8558e9c87f19c845257443f3202d86861c0bc039360138f22d6d0d58f5e157',
        'HOST': 'ec2-54-145-249-177.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_DIR = (BASE_DIR, 'static')

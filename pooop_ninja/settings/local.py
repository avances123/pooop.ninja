from pooop_ninja.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pooopninja',                      
        'HOST': '',
        'PORT': 5433
    }
}

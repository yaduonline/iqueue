from iQueue.settings.base import *

SECRET_KEY = 'uihsdfeqw908084hjhh-hqwen8147nak8l-12jnk9kasd'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'iqueue',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

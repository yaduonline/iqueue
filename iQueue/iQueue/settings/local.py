from iQueue.settings.base import *

DEBUG=True

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

######### LOGGING CONFIG
DEFAULT_LOGGER = 'dev_logger'
######### END

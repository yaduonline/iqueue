from iQueue.settings.base import *

SECRET_KEY = 'sdfnhcc-sdasneh-wewr38r-2hqwe94-iopdsf0'

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

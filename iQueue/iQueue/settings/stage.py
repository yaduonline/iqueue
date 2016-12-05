from iQueue.settings.base import *

DEBUG=False
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

########## AWS CONFIGURATIOM
AWS_ACCESS_KEY_ID = get_env_setting('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_env_setting('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = get_env_setting('AWS_STORAGE_BUCKET_NAME')
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL
AWS_QUERYSTRING_AUTH = False
########## END AWS CONFIGURATION

########## HEROKU DATABASE CONFIGURATION
import dj_database_url
DATABASES = {}
DATABASES['default'] = dj_database_url.config()
########## END HEROKU DATABASE CONFIGURATION

######### LOGGING CONFIG
DEFAULT_LOGGER = 'staging_logger'
######### END

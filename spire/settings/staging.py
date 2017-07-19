from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = True


SOCIAL_AUTH_FACEBOOK_KEY = '1880382195542856'
SOCIAL_AUTH_FACEBOOK_SECRET = 'c203a4edaf5e3896d55ddeb7eab911cb'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.9'
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'locale': 'ru_RU',
  'fields': 'id,name,email'
}

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_basicprofile', 'r_emailaddress']
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ['email-address', 'headline', 'industry']
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [('id', 'id'),
                                   ('firstName', 'first_name'),
                                   ('lastName', 'last_name'),
                                   ('emailAddress', 'email_address')]

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '860sj3h07r7oyz'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'w5Werpj0EiyLh0OQ'


STRIPE_API_KEY = "pk_test_flWrZUy1TeB0z9msSMz67lPY"
STRIPE_SECRET_KEY = "sk_test_es7mrA52AFoENwUyFzOP8SAI"


GOOGLE_MAPS_V3_APIKEY = "AIzaSyAuAQVs-4VRFdR1-9s94H_CxmMr2QLiYpM"
GEO_WIDGET_DEFAULT_LOCATION = { 'lat': '37.4554996','lng': '-122.1996202,11.96' }

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'spire_staging',
        'USER': 'spire',
        'PASSWORD': 'v6Bh0%MJXuXd%G24',
        'HOST': 'localhost',
        'PORT': '',
    }
}
"""



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/spire/error.log',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/spire/access.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

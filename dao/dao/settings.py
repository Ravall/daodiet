# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import platform
# _PATH - путь к manage.py
_PATH = os.path.abspath(os.path.dirname(__file__) + '/../')
DEBUG = platform.node() != 'sancta'
TEMPLATE_DEBUG = DEBUG
SERVER_EMAIL = 'valery.ravall@gmail.com'
ADMINS = (
    ('Ravall', SERVER_EMAIL),
)
MANAGERS = ADMINS

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'dao',
            'USER': 'dao_user',
            'PASSWORD': 'dao_user_password',
            'HOST': '127.0.0.1',
            'PORT': '',
        },
        #'geo': {
        #    'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #    'NAME': 'geodjango',
        #    'USER': 'geo',
        #}
    }
else:
    from dao.production import DATABASES

DJANGO_SETTINGS_MODULE = 'dao.settings'
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['daodiet.ru']

# широта долгота москвы
MSK_LONGITUDE = 37.6156
MSK_LATITUDE = 55.7522

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru'
LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.abspath(os.path.join(_PATH, '../', 'files', 'media'))
#DIRECTORY = '/upload'
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.abspath(
    os.path.join(_PATH, '../', 'files', 'collected_static')
)
STATIC_URL = '/static/'


# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '!6h&0vn+a7(4&cjk*!diyuk!+*&z%jyv-_0k(71dta2^k%8zsk'



MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dao.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'dao.wsgi.application'


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
TEMPLATE_DIRS = (
    os.path.join(_PATH, '../', 'templates')
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request'
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.markup',
    'django.contrib.syndication',
    'south',
    'ipgeo',
    'frontend',
    'mathfilters',
    'compressor',
    'articles',
    'south',
    'dao',
    'markitup'

)
COMPRESS_ENABLED = True
COMPRESS_OUTPUT_DIR = 'min'

#MARKITUP_FILTER = (markdown.markdown, {'safe_mode': True})
JQUERY_URL = '/static/js/lib/jquery.js'

COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
    ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
    ('text/stylus', 'stylus < {infile} > {outfile}'),
)

# для пакета pygeoip
# http://dev.maxmind.com/geoip/install/city
GEO_CITY_DAT_FILE = '/usr/local/share/GeoIP/GeoLiteCity.dat'


DISQUS_USER_API_KEY = '5oG2QS96wI89LRzjhWz8BAVn9csjCug8PoInnFrxWkaApYHMv8tVpUaRLuvMi7lr'
DISQUS_FORUM_SHORTNAME = 'DaoDiet'

#ARTICLES_TEASER_LIMIT = 75
#ARTICLES_AUTO_TAG = True
#ARTICLES_DEFAULT_DB = 'default'
#ARTICLES_LOOKUP_LINK_TITLE = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

from dao.ayurveda_config import *

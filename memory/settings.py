# -*- coding: utf-8 -*-
import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG

APP_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = os.path.abspath(os.path.dirname(APP_DIR))
#
#GRAPPELLI_ADMIN_TITLE = u'我的足迹 - - 后台管理系统'
#
## Full filesystem path to the project.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
#
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'

THUMBNAIL_MEDIA_ROOT = MEDIA_ROOT

#THUMBNAIL_MEDIA_URL = MEDIA_URL 
#
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"


SITE_TITLE = 'memory'


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

try:
    import sae.const
except:
    pass
from os import environ
#根据环境定义数据库连接参数
islocalhost = not environ.get("APP_NAME","")

if islocalhost:
    mysql_name = 'memory'
    mysql_user = 'root'
    mysql_pass = ''
    mysql_host = '127.0.0.1'
    mysql_port = '3306'
    mysql_host_s = '127.0.0.1'
    DEBUG = True
else:#sae上
    mysql_name = sae.const.MYSQL_DB
    mysql_user = sae.const.MYSQL_USER
    mysql_pass = sae.const.MYSQL_PASS
    mysql_host = sae.const.MYSQL_HOST
    mysql_port = sae.const.MYSQL_PORT
    mysql_host_s = sae.const.MYSQL_HOST_S
    DEBUG = True


DATABASES = {
    "default": {
        # Add "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.mysql",
        # DB name or path to database file if using sqlite3.
        "NAME": mysql_name,
        # Not used with sqlite3.
        "USER": mysql_user,
        # Not used with sqlite3.
        "PASSWORD": mysql_pass,
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": mysql_host,
        # Set to empty string for default. Not used with sqlite3.
        "PORT": mysql_port,
    },
    "master": {
        # Add "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.mysql",
        # DB name or path to database file if using sqlite3.
        "NAME": mysql_name,
        # Not used with sqlite3.
        "USER": mysql_user,
        # Not used with sqlite3.
        "PASSWORD": mysql_pass,
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": mysql_host,
        # Set to empty string for default. Not used with sqlite3.
        "PORT": mysql_port,
    },
    "slave": {
        # Add "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.mysql",
        # DB name or path to database file if using sqlite3.
        "NAME": mysql_name,
        # Not used with sqlite3.
        "USER": mysql_user,
        # Not used with sqlite3.
        "PASSWORD": mysql_pass,
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": mysql_host_s,
        # Set to empty string for default. Not used with sqlite3.
        "PORT": mysql_port,
    }        
}
class DataBaseRouter(object):
    """
    A router to control all database operations.
    """
    def db_for_read(self, model,  *args, **kwargs):
        """
        Attempts to read.
        """
        return "slave"

    def db_for_write(self, model,  *args, **kwargs):
        """
        Attempts to write .
        """
        return "master"
       
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation between two objects in the db pool"
        db_list = ('master','slave')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_syncdb(self, db, model):
        "Explicitly put all models on all databases."
        return True
       
       
DATABASE_ROUTERS = [DataBaseRouter()]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


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
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8c^ael95%*u&amp;9r3u47lp!%jqc$#^u3mqw(l+%xt2qw&amp;=xw&amp;ygv'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'memory.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'memory.wsgi.application'

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)

INSTALLED_APPS = (
    'grappelli',
    "django.contrib.admin",
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'memory',
    'easy_thumbnails',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)


THUMBNAIL_ALIASES = {
    '': {
        'mini': {'size': (48, 48), 'crop': True},
        'small': {'size': (64, 64)},
        'normal': {'size': (192, 0), 'crop': True},
        'big': {'size': (384, 0), 'crop': True},
        "large": {'size':(650,0)},
        "avatar": {'size':(64,64)},
        "avatar_normal": {'size':(128,128)},
        "avatar_large": {'size':(192, 192)},
    },
}

THUMBNAIL_SUBDIR = "thumbs"
THUMBNAIL_EXTENSION = "png"

TEMPLATE_CONTEXT_PROCESSORS = (
   "django.contrib.auth.context_processors.auth",
   "django.core.context_processors.request",
   "django.core.context_processors.i18n",
   'django.core.context_processors.static',
   "django.core.context_processors.media",
   "django.contrib.messages.context_processors.messages",
)

GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'

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

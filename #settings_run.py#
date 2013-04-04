# _*_ coding: utf-8 _*_
# Django settings for task project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'task',                      # Or path to database file if using sqlite3.
        'USER': 'xia',                      # Not used with sqlite3.
        'PASSWORD': 'c2vm.c0m',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-cn'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = ''
STATIC_URL = '/static/'
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
SECRET_KEY = 'vq(r0czdf&amp;b_z=#w@(v!&amp;u&amp;5&amp;2w6nvkw3-gch+wf=6q@*s8qrn'

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

ROOT_URLCONF = 'task.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'task.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'django.contrib.admin',
     'djcelery',
     'task',
)# A sample logging configuration. The only tangible logging

BROKER_HOST = "localhost"
BROKER_BACKEND="redis"
REDIS_PORT=6379
REDIS_HOST = "localhost"
BROKER_USER = ""
BROKER_PASSWORD =""
BROKER_VHOST = "0"
REDIS_DB = 0
REDIS_CONNECT_RETRY = True
CELERY_SEND_EVENTS=True
CELERY_RESULT_BACKEND='redis'
CELERY_TASK_RESULT_EXPIRES =  10
CELERYBEAT_SCHEDULER="djcelery.schedulers.DatabaseScheduler"
ELERY_ALWAYS_EAGER=True
import djcelery
djcelery.setup_loader()

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
DB_NAME = "xia"
PAGE_LIMIT = 10
DEFAULT_LIMIT = 10
DEBUG = True
#状态码
ST_CODE = {
    'norm': 0,
    'del': 1,
    'v': 2,
}
# one or more directories
MAKO_DIR = 'templates'
# optional, if specified Mako will cache to this directory
MAKO_CACHEDIR = '/tmp/mako'
# optional, if specified Mako will respect the cache size
MAKO_CACHESIZE = 500
CONTENT_TYPE_LIST = [
    "audio/midi",                     
    "audio/mpeg",                      
    "audio/ogg",                       
    "audio/x-m4a",                     
    "audio/x-realaudio",               
    "video/3gpp",                      
    "video/mp4",                       
    "video/mpeg",                      
    "video/quicktime",                 
    "video/webm",                      
    "video/x-m4v",                     
    "video/x-mng",                     
    "video/x-ms-asf",                  
    "video/x-ms-wmv",                      
    "video/x-msvideo",                     
]
PLAY_LIST_TYPE = ["Audio", "Video", "VideoRecording", "AudioRecording"]

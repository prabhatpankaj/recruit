import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '4lydncnn3czegjb&#)od!2g4v$7=ub!2ovnqot_**93rwt6=qq'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # External apps
    'django_extensions',
    'django_countries',
    'bootstrap3',
    'storages',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Project apps
    'accounts',
    'employers',
    'jobs',
    'interviews',
    'recruiters',
    'candidates',
    'dashboards',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
]


ROOT_URLCONF = 'recruit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'recruit.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static_root")

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static", "static_files"),
)

PHONENUMBER_DB_FORMAT = 'E164'

import authkey

if DEBUG:
    AWS_STORAGE_BUCKET_NAME = authkey.AWS_STORAGE_BUCKET_NAME
    AWS_ACCESS_KEY_ID = authkey.AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY = authkey.AWS_SECRET_ACCESS_KEY
else:
    if 'AWS_STORAGE_BUCKET_NAME' in os.environ:
        AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
        AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
        AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    else:
        AWS_STORAGE_BUCKET_NAME = authkey.AWS_STORAGE_BUCKET_NAME
        AWS_ACCESS_KEY_ID = authkey.AWS_ACCESS_KEY_ID
        AWS_SECRET_ACCESS_KEY = authkey.AWS_SECRET_ACCESS_KEY
    if 'AWS_CLOUDFRONT_DOMAIN' in os.environ:
        AWS_CUSTOM_DOMAIN = os.environ['AWS_CLOUDFRONT_DOMAIN']
    else:
        AWS_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
        AWS_S3_HOST = authkey.AWS_S3_HOST
    AWS_HEADERS = {
        'Expires': 'Thu, 31 Jan 2030 20:00:00 UTC',
        'Cache-Control': 'max-age=94608000',
    }

if DEBUG:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
    MEDIA_URL = '/media/'
else:
    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'recruit.custom_storages.StaticStorage'
    STATIC_URL = 'https://%s/%s/' % (AWS_CUSTOM_DOMAIN, STATICFILES_LOCATION)

    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = 'https://%s/%s/' % (AWS_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'recruit.custom_storages.MediaStorage'

# All auth configurations
ACCOUNT_ADAPTER = 'accounts.adapter.MyAccountAdapter'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATON_AUTHENTICATED_REDIRECT_URL = None

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[RECRUIT]: '
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'

ACCOUNT_LOGOUT_ON_GET = False
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_SIGNUP_FORM_CLASS = None
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_USER_MODEL_EMAIL_FIELD = 'email'

ACCOUNT_USERNAME_MIN_LENGTH = 5
ACCOUNT_USERNAME_BLACKLIST = []
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_PASSWORD_INPUT_REMINDER_VALUE = False
ACCOUNT_PASSWORD_MIN_LENGTH = 6
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# Sendgrid Email API Configuration
EMAIL_BACKEND = "sgbackend.SendGridBackend"

if DEBUG:
    SENDGRID_USER = authkey.SENDGRID_USER
    SENDGRID_PASSWORD = authkey.SENDGRID_PASSWORD
else:
    if 'SENDGRID_USER' in os.environ:
        SENDGRID_USER = os.environ['SENDGRID_USER']
        SENDGRID_PASSWORD = os.environ['SENDGRID_PASSWORD']
    else:
        SENDGRID_USER = authkey.SENDGRID_USER
        SENDGRID_PASSWORD = authkey.SENDGRID_PASSWORD

from django.contrib import messages
MESSAGE_TAGS = {messages.DEBUG: 'debug',
                messages.INFO: 'info',
                messages.SUCCESS: 'success',
                messages.WARNING: 'warning',
                messages.ERROR: 'danger'}

# django-countries configuration
COUNTRIES_FIRST_REPEAT = True
COUNTRIES_FIRST_BREAK = 'Select country'
COUNTRIES_FIRST = [
    'US',
    'CA',
    'GB',
    'IE',
    'AU',
    'NZ',
    'ZA'
]

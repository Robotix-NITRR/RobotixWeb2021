import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h5au0+ubk)_fy#y)xw(-kotofkgj^&ca9fb9ovkm=z1+8ez2zv'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['robotix.nitrr.ac.in','192.46.213.171']

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #our apps
    'about',
    'events',
    'gallery',
    'achievements',
    'contact',
    'extras',
    'alumni',
    'users',
    'roboPortal',
    'workshops',
    'roboexpo',
    'certificate',

    #frameworks
    'import_export',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'django_crontab',

    #social login
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.google',
    'django.contrib.admin',
]

SITE_ID = 1

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
OLD_PASSWORD_FIELD_ENABLED = True
LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'


REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "users.serializers.UserDetailsSerializer",
}#DEBUG = TrueUserProfileSerializer",


ACCOUNT_ADAPTER = 'users.adapter.CustomAccountAdapter'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'RobotixWeb.urls'
templates_dir = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [templates_dir,],
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

WSGI_APPLICATION = 'RobotixWeb.wsgi.application'


# Database
if DEBUG:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'robotixdb3',
            'USER': 'robot',
            'PASSWORD' :'django',
            'HOST' : 'localhost',
            'PORT' : ''

        }

    }
# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



STATIC_URL = '/static/'

if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),]
else :
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

AUTH_USER_MODEL = 'users.UserProfile'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

if DEBUG:
    EMAIL_HOST_USER = 'wandavision5432@gmail.com'
else :
    EMAIL_HOST_USER = 'robotixclub@nitrr.ac.in'
    #EMAIL_HOST_USER = 'wandavision5432@gmail.com'

EMAIL_HOST_PASSWORD = 'Nitrrobots16'

# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
LOGOUT_REDIRECT_URL = '/'

#crontab
CRONJOBS = [
    ('*/1 * * * *', 'certificate.cron.email_job'),
    ('*/1 * * * *', 'certificate.cron.cert_job')
]
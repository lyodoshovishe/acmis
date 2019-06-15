"""
Django settings for acis project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from dotenv import load_dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(os.path.join(BASE_DIR, '.env'))

ENV = os.getenv('ENV')

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y+cz5bss=pao3ehe*v$5u+5d8yoo99)9&bm1+&=fnzxfznbg=r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', True) == 'True'

# Application definition
INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.sitemaps',
    'taggit',
    'mptt',
    'tracking',
    'cms',
    'django.contrib.admin',
    'ckeditor',
    'django_bleach',
    'ban',
    'django_messages',
    'captcha',
    'hitcount',
    'simplemde',
    'django_user_agents',
    'tracking_analyzer',
]

MIDDLEWARE = [
#    'csp.middleware.CSPMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'ban.middleware.BanManagement',
    'cms.midlewares.XForwardedForMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'tracking.middleware.VisitorTrackingMiddleware',
]

ROOT_URLCONF = 'acis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'cms.context_processors.export_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'acis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DBNAME', 'postgres'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', 5432),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'default-cache'
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'uk'
LANGUAGES = (
    ('uk', 'Ukrainian'),
)

TIME_ZONE = 'Europe/Kiev'

USE_I18N = False
USE_L10N = True
USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

FILE_UPLOAD_PERMISSIONS = 0o755
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_ALLOW_NONIMAGE_FILES = False

ACCOUNT_ACTIVATION_DAYS = 2
REGISTRATION_OPEN = True
REGISTRATION_SALT = 'FfjoH3YJSavC67d6MvZCzAUGZJluMJqYlZ10WqLfPM79uydOe4CqMQMuJWeie9yA'

EMAIL_HOST = os.getenv('EMAIL_HOST', 'localhost')
EMAIL_PORT = os.getenv('EMAIL_PORT', 25)
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', False) == 'True'
DEFAULT_FROM_EMAIL = 'noreply@diggers.kiev.ua'

BLEACH_ALLOWED_TAGS = [
  'p',
  'b',
  'i',
  'u',
  'em',
  'strong',
  'a',
  'table',
  'tr',
  'td',
  'th',
  'thead',
  'tbody',
  'caption',
  'hr',
  'span',
  'img',
  'br',
  'iframe',
  'figcaption',
  'figure',
]
BLEACH_ALLOWED_ATTRIBUTES = ['href', 'title', 'style', 'cellpadding', 'cellspacing', 'border', 'target', 'alt', 'src', 'allowfullscreen', 'frameborder', 'height', 'width']
BLEACH_ALLOWED_STYLES = [
  'font-family',
  'font-weight',
  'text-decoration',
  'font-variant',
  'background-color',
  'border-color',
  'border-style',
  'border-width',
  'float',
  'text-align',
  'vertical-align',
  'width',
  'height',
  'width',
  'color',
  'margin'
]
BLEACH_STRIP_TAGS = True
BLEACH_STRIP_COMMENTS = False
BLEACH_ALLOWED_IFRAME_SRC = [
  'youtube.com',
  'www.youtube.com',
]

AVATAR_MAX_WIDTH = 80
AVATAR_MAX_HEIGHT = 80
AVATAR_DEFAULT = STATIC_URL + 'images/no_avatar.png'
AVATAR_DIMENSIONS = '%sx%s' % (AVATAR_MAX_WIDTH, AVATAR_MAX_HEIGHT,)

DEFAULT_REGISTRATION_GROUP = 'Users'

PAGINATION_POSTS_COUNT = 25
PAGINATION_USERS_COUNT = 50

SESSION_SAVE_EVERY_REQUEST = True

ALLOWED_HOSTS = [
    'www.diggers.kiev.ua',
    'diggers.kiev.ua',
    '159.65.127.90',
    '127.0.0.1',
]

RECAPTCHA_PUBLIC_KEY = '6LegnF0UAAAAAIbP1Xu21W_e6kObQIOYbqFs2VBC'
RECAPTCHA_PRIVATE_KEY = '6LegnF0UAAAAAONkfdiI5dU1MhqA2BAvQsaGI2bp'
NOCAPTCHA = True

TAGTOOLS_CLOUD_STEPS = 6
TAGTOOLS_CLOUD_MIN_COUNT = 1

OPENGRAPH_CONFIG = {
    'FB_ADMINS': '',
    'FB_APP_ID': '',
    'DEFAULT_IMAGE': '%simages/og_image.png' % STATIC_URL,
    'SITE_NAME': 'Сайт диггеров Киева',
}

# Number of seconds of inactivity before a user is marked offline
USER_ONLINE_TIMEOUT = 60 * 15

GEOIP_PATH = os.path.join(BASE_DIR, 'geoip-data')

TRACK_USING_GEOIP = True
TRACK_REFERER = True
TRACK_PAGEVIEWS = True

TRACK_IGNORE_URLS = (
    r'^(favicon\.ico|robots\.txt|sitemap\.xml)$',
    r'^admin(?!/login).*$',
    r'^ajax/tags',
    r'^ckeditor',
    r'^latest/feed',
    r'^static/'
    # No need. This track by another tracking
    r'^post/\d',
    r'^category/\w+',
)

CKEDITOR_CONFIGS = {
    'default': {
        'filebrowserBrowseUrl': '',
        'filebrowserImageBrowseUrl': '',
        'filebrowserFlashBrowseUrl': '',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Youtube', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'], ['Source'],
        ],
        'extraPlugins': ','.join([
          'youtube',
          'autoembed',
          'image2'
        ])
    }
}

SIMPLEMDE_OPTIONS = {
    'placeholder': 'Комментар',
    'status': False,
    'autosave': {
        'enabled': True
    },
    'spellChecker': False,
    'forceSync': True,
}

'''
CSP_DEFAULT_SRC = ("'self'")
CSP_SCRIPT_SRC = ("'self'", 'https://www.google.com/recaptcha/', 'https://www.gstatic.com/recaptcha/')
CSP_FRAME_SRC = ('https://www.google.com/recaptcha/')
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")
CSP_FONT_SRC = ("'self'")
CSP_IMG_SRC = ("'self'")
'''

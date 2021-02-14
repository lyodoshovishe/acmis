"""
Django settings for diggers.kiev.ua project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
    'cms',
    'django.contrib.admin',
    'ckeditor',
    'django_bleach',
    'captcha',
    'simplemde',
    'webpush',
    'social_django',

    # Custom vendored packages
    'vendors.django_messages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middlewares.XForwardedForMiddleware',
    'cms.middlewares.BanManagement',
    'cms.middlewares.ActiveUserMiddleware',
    'cms.middlewares.OnlineUsersMiddleware',
]

ROOT_URLCONF = 'diggers.urls'

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
                'django.template.context_processors.media',
                'cms.context_processors.export_settings',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'diggers.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'postgres'),
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
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.instagram.InstagramOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'uk-UK'
LANGUAGES = (
    ('uk', 'Ukrainian'),
)

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True
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
  'h2',
  'h3',
  'h4',
  'h5',
  'h6',
  'span',
  'img',
  'br',
  'iframe',
  'figcaption',
  'figure',
  'pre',
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


AVATAR_DEFAULT =  '%simages/no_avatar.png' % STATIC_URL
AVATAR_SIZE = (80, 80)
IMAGES_SIZE = 1280

DEFAULT_REGISTRATION_GROUP = 'Users'

PAGINATION_POSTS_COUNT = 25
PAGINATION_USERS_COUNT = 50
PAGINATION_MAPS_COUNT = 50

SESSION_SAVE_EVERY_REQUEST = True

ALLOWED_HOSTS = [
    'www.diggers.kiev.ua',
    'diggers.kiev.ua',
    '142.93.107.25',
    '127.0.0.1',
]

RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY', '')
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY', '')
NOCAPTCHA = True

TAGTOOLS_CLOUD_STEPS = 6
TAGTOOLS_CLOUD_MIN_COUNT = 1

OPENGRAPH_CONFIG = {
    'FB_ADMINS': '',
    'FB_APP_ID': '',
    'DEFAULT_IMAGE': 'images/og_image.png',
    'SITE_NAME': 'Сайт дигерів Києва',
}

# Number of seconds of inactivity before a user is marked offline
USER_ONLINE_TIMEOUT = 60 * 15
CKEDITOR_CONFIGS = {
    'default': {
        'format_tags': 'p;h2;h3;h4;h5;h6;pre',
        'width': '99%',
        'filebrowserBrowseUrl': '',
        'filebrowserImageBrowseUrl': '',
        'filebrowserFlashBrowseUrl': '',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Youtube', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'], ['Source'],
        ],
        'removePlugins': 'image',
        'extraPlugins': ','.join([
          'youtube',
          'autoembed',
          'image2'
        ]),
        'contentsCss': [
            '/static/ckeditor/ckeditor/contents.css',
            '/static/css/ckeditor_contents.css',
        ],
    }
}


SIMPLEMDE_OPTIONS = {
    'placeholder': 'Коментар',
    'status': False,
    'autosave': {
        'enabled': True
    },
    'spellChecker': False,
    'forceSync': True,
}

WEBPUSH_SETTINGS = {
    'VAPID_PUBLIC_KEY': os.getenv('VAPID_PUBLIC_KEY', ''),
    'VAPID_PRIVATE_KEY': os.getenv('VAPID_PRIVATE_KEY', ''),
    'VAPID_ADMIN_EMAIL': 'admin@diggers.kiev.ua'
}

WEBPUSH_ICON_URL = 'https://diggers.kiev.ua/static/images/og_image.png'

SOCIAL_AUTH_POSTGRES_JSONFIELD = True
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY', '')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET', '')

SOCIAL_AUTH_FACEBOOK_KEY = os.getenv('SOCIAL_AUTH_FACEBOOK_KEY', '')
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv('SOCIAL_AUTH_FACEBOOK_SECRET', '')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link', 'user_gender', 'user_birthday']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'fields': 'id, name, email, picture.type(large), link, gender, birthday'
}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [
    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'picture'),
    ('link', 'profile_url'),
    ('gender', 'gender'),
    ('birthday', 'birthday')
]

SOCIAL_AUTH_GITHUB_KEY = os.getenv('SOCIAL_AUTH_GITHUB_KEY', '')
SOCIAL_AUTH_GITHUB_SECRET = os.getenv('SOCIAL_AUTH_GITHUB_SECRET', '')

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'cms.pipeline.load_user',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'cms.pipeline.save_profile',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

PAYPAL_BUTTON_ID = os.getenv('PAYPAL_BUTTON_ID', '')

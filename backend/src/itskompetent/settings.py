"""
Django settings for itskompetent project.

Generated by 'django-admin startproject' using Django 4.0.3.

"""

import os
from pathlib import Path
import os
from django.core.exceptions import ImproperlyConfigured

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = f"Set the {var_name} environment variable"
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')


DEBUG = True
ALLOWED_HOSTS = ['*']

HTTP_MODE = True

DOMAIN_URL=get_env_variable('API_URL')
# Application definition
CSRF_COOKIE_AGE = None
SESSION_EXPIRE_AT_BROWSER_CLOSE = True




# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'users',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djoser',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'import_export',
    'corsheaders',
    'polymorphic',
    'django_filters',
    'job_profiles',
    'threats',
    'competence_tests',
    'trainings',
    'campagne'
]
CORS_ALLOWED_ORIGINS = [
"http://XXX.XXX.XX",
]

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = ["http://XXX.XXX.XX"]

from datetime import timedelta

#For RSA KEY USAGE

""" BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to the RSA keys
RSA_PRIVATE_KEY_PATH = os.path.join(BASE_DIR, 'keys', 'mykey')
RSA_PUBLIC_KEY_PATH = os.path.join(BASE_DIR, 'keys', 'mykey.pub')

# Read the private key
with open(RSA_PRIVATE_KEY_PATH, 'r') as key_file:
    RSA_PRIVATE_KEY = key_file.read()

# Read the public key
with open(RSA_PUBLIC_KEY_PATH, 'r') as key_file:
    RSA_PUBLIC_KEY = key_file.read() """

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(seconds=300),  # Set to your desired lifetime
    'REFRESH_TOKEN_LIFETIME': timedelta(seconds=18000),  # Set to your desired lifetime
    'ROTATE_REFRESH_TOKENS': True,  # enable refresh token rotation
    'BLACKLIST_AFTER_ROTATION': True,  # enable blacklisting for older refresh tokens
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None ,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

}

# FOR RSA USAGE
""" SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(seconds=300),  # Set to your desired lifetime
    'REFRESH_TOKEN_LIFETIME': timedelta(seconds=18000),  # Set to your desired lifetime
    'ROTATE_REFRESH_TOKENS': True,  # enable refresh token rotation
    'BLACKLIST_AFTER_ROTATION': True,  # enable blacklisting for older refresh tokens
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'ALGORITHM': 'RS256',
    'SIGNING_KEY': RSA_PRIVATE_KEY,
    'VERIFYING_KEY': RSA_PUBLIC_KEY,
    'VERIFYING_KEY': None ,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

} """



REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
     'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
   'DEFAULT_AUTHENTICATION_CLASSES': (
        'users.backends.CookieJWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    
    
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'users.middlewares.JWTWithCSRFMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'users.middlewares.EnforcePasswordChangeMiddleware'
]

ROOT_URLCONF = 'itskompetent.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'itskompetent.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_env_variable('DB_NAME'),
        'USER': get_env_variable('DB_USER'),
        'PASSWORD': get_env_variable('DB_PASS'),
        'HOST': get_env_variable('DB_HOST'),
        'PORT': '3306',  # The port inside the container remains 3306
    }
}





LOGIN_URL = '/accounts/login/'
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'de'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = get_env_variable('API_URL') + '/static/'


STATIC_ROOT = '/code/src/staticfiles'




# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Base url to serve media files
MEDIA_URL = get_env_variable('API_URL')+ '/media/backend/'
# Path where media is stored
MEDIA_ROOT = '/code/src/media'

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_header": "ITS.kompetent Admin Login",
    "welcome_sign": "Wilkommen beim ITS.kompetent Admin Portal",
    "site_brand": None,
    "related_modal_active": True,
    "use_google_fonts_cdn":False,
    #"site_icon":"images/k.png",
    #"site_logo": "images/ITS_Kompetent_Logo.svg",
    #"login_logo": "images/ITS.Kompetent_Logo.png",
    #"login_logo_dark": "images/ITS_Kompetent_Logo.svg",
    "copyright": "ITS.kompetent",
    "changeform_format": "horizontal_tabs",

}
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    #"brand_colour": "navbar-light",
    "accent": "accent-primary",
    #"navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    }
}






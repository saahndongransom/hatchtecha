"""
Django settings for techsonia project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES_DIR = os.path.join(BASE_DIR, 'nblog/templates')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p$ks)ozh-%-4&nrq0)f5e&x081+ne!#1ou*@0h#%888^d1nc8*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nblog',
    'ckeditor',
    'paypal.standard.ipn',
    'crispy_forms',
    'tinymce',
    'django.contrib.sites',

    # django_comments_xtd and django_comments order should be same
    'django_comments_xtd',
    'django_comments',
    'taggit',
    'django_social_share',
    



    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'newhatchblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',


        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'newhatchblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL ='/images/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'newhatchblog/static')
]
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#paypal setting
PAYPAL_TEST = True
PAYPAY_RECEIVES_EMAIL ='saahndongransom@gmail.com'



SITE_ID = 1
COMMENTS_APP = 'django_comments_xtd'

COMMENTS_XTD_MAX_THREAD_LEVEL = 3

COMMENTS_XTD_CONFIRM_EMAIL =False
#  To help obfuscating comments before they are sent for confirmation.
COMMENTS_XTD_SALT = (b"Timendi causa est nescire. "
                     b"Aequam memento rebus in arduis servare mentem.")

# Source mail address used for notifications.
COMMENTS_XTD_FROM_EMAIL = "saahndongransom@gmail.com"

# Contact mail address to show in messages.
COMMENTS_XTD_CONTACT_EMAIL = "helpdesk@example.com"
COMMENTS_XTD_MAX_THREAD_LEVEL = 1  # default is 0
COMMENTS_XTD_LIST_ORDER = ('-thread_id', 'order')  # default is ('thread_id', 'order')
COMMENTS_XTD_MAX_THREAD_LEVEL = 0  # site wide default
COMMENTS_XTD_MAX_THREAD_LEVEL_BY_APP_MODEL = {
    # Objects of the app blog, model post, can be nested
    # up to thread level 1.
        'nblog.post': 1,
}
COMMENTS_XTD_APP_MODEL_OPTIONS = {
    'default': {
        'allow_flagging': False,
        'allow_feedback': False,
        'show_feedback': False,
        'who_can_post': 'all'  # Valid values: 'all', users'
    }
}

# Either enable sending mail messages to the console:
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# or smpt EmailBackend

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Or set up the EMAIL_* settings so that Django can send emails:
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'saahndongransom@gmail.com'
EMAIL_HOST_PASSWORD = 'ymsezdinahtijcly'
DEFAULT_FROM_EMAIL = "Helpdesk <helpdesk@yourdomain>"



#paypay setting
PAYPAL_TEST = True
PAYPAl_RECEIVER_EMAIL = 'sandbox@gmail.com'

TEMPLATE_LOADERS = (
    'django.article_utils.loaders.nblog.load_template_source',
)

ALLOWED_HOSTS = ['*']

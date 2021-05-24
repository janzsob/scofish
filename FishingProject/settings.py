"""
Django settings for FishingProject project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import sys
import django_heroku
import dj_database_url
from decouple import config
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
""" CHANGE IT IN PRODUCTION! """
DEBUG = True

ALLOWED_HOSTS = ['scofish.herokuapp.com', '127.0.0.1', 'www.scofish.net', 'scofish.net']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication', # app
    'new_trip', # app
    'trips_feed', # app
    'catch_details', # app
    'stats', # app
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FishingProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'FishingProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

pg_password = os.environ.get("postgresgl_password")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Fishing_Project_DB',
        'USER': 'postgres',
        'PASSWORD': pg_password,
        'HOST': 'localhost',
        "PORT": "5432",
    }
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'hu' #'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# when login required is activated
LOGIN_URL = "auth:login"


STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'), # to find that static folder that aren't tied to a particular app
)

# in production
if DEBUG == False:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEADIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# for heroku deployment
""" CHANGE IT IN PRODUCTION! """
#django_heroku.settings(locals())


#S3 BUCKETS CONFIG (deployment)
""" CHANGE IT IN PRODUCTION! """
"""
AWS_ACCESS_KEY_ID = 'AKIAU3UJGCF7ASABZREK'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'scofish.net-bucket'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_REGION_NAME = 'eu-central-1' 
AWS_S3_SIGNATURE_VERSION = 's3v4'
"""
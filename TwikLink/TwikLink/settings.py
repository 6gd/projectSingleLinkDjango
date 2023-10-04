"""
Django settings for TwikLink project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h2axrib3p&ga9-3-f2^f7&+^o2gr7w#7fj%7kso3#_!z+af^7g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # 'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'colorfield',
    'Profile',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

SITE_ID = 1
ACCOUNT_FORMS = {'signup': 'mysite.forms.MyCustomSignupForm'}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TwikLink.urls'

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
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'TwikLink.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
databaseurl = "postgres://mahdi_user:kpTZqNfCvbvUK8GsFa9EBmWGDhbCBnuK@dpg-ckbbp0pme4lc7384a18g-a.oregon-postgres.render.com/mahdi"
DATABASES = {
    'default': dj_database_url.config(
        default=databaseurl
    )
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         "NAME": "TwikLink",
#         "USER": "postgres",
#         "PASSWORD": "toor",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# STATIC_URL = '/static/'
# STATICFILES_DIRS  = [os.path.join(BASE_DIR,'TwikLink/static'),]
# STATIC_ROOT = os.path.join(BASE_DIR,'static')

# MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# MEDIA_URL = '/media/'



STATIC_URL = '/static/'

MEDIA_URL = '/media/'


if DEBUG:

    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'TwikLink/static')]

else:

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True

LOGIN_REDIRECT_URL = '/login'

ACCOUNT_EMAIL_REQUIRED =True
ACCOUNT_FORMS = {
    'signup': 'Profile.forms.MyCustomSignupForm',
    'login': 'Profile.forms.MyCustomLoginForm',
    'change_password': 'Profile.forms.ChangePasswordMyForm',
}
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS =True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_EMAIL_VERIFICATION = "none"
# ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True


# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Use SMTP for sending emails
EMAIL_HOST = 'smtp.gmail.com'  # Replace with your SMTP server address
EMAIL_PORT = 587  # Port for your SMTP server (587 is the common port for TLS)
EMAIL_USE_TLS = True  # Use TLS for secure communication with the SMTP server
EMAIL_HOST_USER = 'mahdibaibaa@gmail.com'  # Your email address for sending emails
EMAIL_HOST_PASSWORD = 'dabw kqxr wevd caqr'  # Your email password

ACCOUNT_PASSWORD_RESET_KEY_SUBJECT = 'account/email/password_reset_key_subject.txt'
ACCOUNT_PASSWORD_RESET_TIMEOUT = 30

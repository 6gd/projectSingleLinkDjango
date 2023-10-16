from pathlib import Path
import os
import dj_database_url
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent




SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG",cast=bool)


ALLOWED_HOSTS = ["mahdi-ggerftgd.koyeb.app"]



INSTALLED_APPS = [
    'admin_interface',
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
    'whitenoise.runserver_nostatic',
    "debug_toolbar",
    # 'defender',

]

SITE_ID = 1
ACCOUNT_FORMS = {'signup': 'mysite.forms.MyCustomSignupForm'}

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # 'defender.middleware.FailedLoginMiddleware',
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
databaseurl = "postgres://gg_wcqa_user:bCGbrMCeXlWJlG8kAXNV4nZ9g3fcEAJC@dpg-ckm24co710pc73euo3ag-a.frankfurt-postgres.render.com/gg_wcqa"
DATABASES = {
    'default': dj_database_url.config(
        default=databaseurl
    )
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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = '/static/'
STATICFILES_DIRS  = [os.path.join(BASE_DIR,'TwikLink/static'),]
STATIC_ROOT = os.path.join(BASE_DIR,'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

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


ACCOUNT_EMAIL_SUBJECT_PREFIX = "TwikLink"

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 86400
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
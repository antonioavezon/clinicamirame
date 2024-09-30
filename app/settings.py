import os
from datetime import datetime
from pathlib import Path

# BASE_DIR es el directorio base de tu proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Nivel de verbosidad para los logs, se puede cambiar fácilmente
nivel = "DEBUG"  # Puedes cambiar esto a "INFO", "WARNING", "ERROR", etc.

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Directorio donde se guardarán los logs
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# Asegurarse de que el directorio de logs exista
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Archivos de log para Django y la aplicación
DJANGO_LOG_FILENAME = os.path.join(LOG_DIR, f'django_{datetime.now().strftime("%Y%m%d")}.log')
APP_LOG_FILENAME = os.path.join(LOG_DIR, f'app_{datetime.now().strftime("%Y%m%d")}.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        # Handler para los logs de Django
        'django_file': {
            'level': nivel,  # Usamos la variable nivel para controlar la verbosidad
            'class': 'logging.FileHandler',
            'filename': str(DJANGO_LOG_FILENAME),
            'formatter': 'verbose',
        },
        # Handler para los logs de la aplicación
        'app_file': {
            'level': nivel,  # Usamos la variable nivel para controlar la verbosidad
            'class': 'logging.FileHandler',
            'filename': str(APP_LOG_FILENAME),
            'formatter': 'verbose',
        },
    },
    'formatters': {
        'verbose': {
            'format': '{asctime} {levelname} {name} {message}',
            'style': '{',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['django_file'],
            'level': nivel,  # Usamos la variable nivel para controlar la verbosidad
            'propagate': True,
        },
        'app_logger': {
            'handlers': ['app_file'],
            'level': nivel,  # Usamos la variable nivel para controlar la verbosidad
            'propagate': True,
        },
    },
}

SECRET_KEY = 'django-insecure-4^v4zi3_(a%rrf60zab!3^vczj0mp1@7^o4z!5)l4s=q(wbgg2'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'welcome',
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

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

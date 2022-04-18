"""
Django settings for django_api1 project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
#-------  BASE_DIR---------
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# Este es el directorio don de se encuentra nuestro proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# --------------- SECRET KEY -----------------s
#  nuestra llave secreta única generada por cada proyecto
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mwq=nd^-c+8xwoxh5u(+3@7cx4%5^l#0tn6umw)%npo*5d2*u5'


#------------ DEGUG -----------------
# si queremos activar que nos detecte errores, esto en producción suele estar a FALSE
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#------------- HOST ------------------
# > el host donde irá alojada nuestra aplicación suele
# ponerse “*” para permitir cualquiera, esto se emplea en producción
ALLOWED_HOSTS = []


#--------- INSTALLED APPS -------------
# Application definition
# Cada vez que creamos una nueva app en nuestro proyecto la registramos aqui
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Cada app que creamos la debemos añadir aqui
    'apptest',

]

#------------- MIDDLEWARE -----------------
# > necesario para describir los controles en la aplicación
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#------------- URLs -------------------
# ruta de las urls principales
ROOT_URLCONF = 'django_api1.urls'

#--------------- TEMPLATES -------------
# ruta dónde se encuentra nuestras plantillas html
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

# ------------- WSGI ---------------
# esto se emple en producción para dar la ruta del archivo wsgi.py
WSGI_APPLICATION = 'django_api1.wsgi.application'


# ------ DATABASE ----------------
# conexión a la base de datos esto se hace genera por
# defecto al crear la aplicación si necesitamos otra conexión a otra base de
# datos, la describimos en este punto
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
#  lenguaje principal de la aplicación
LANGUAGE_CODE = 'en-us'

 # Modificar hora --> zona horaria donde nos encontramos
TIME_ZONE = 'Europe/Madrid'

# permitido cambio de idiomas
USE_I18N = True

USE_L10N = True

USE_TZ = True

#------------------------------------------------------------------
# -------------------   ADD ROUTES  -------------------------------
# A continuación, añadiremos al archivo settings.py las rutas de las carpetas
#necesarias para trabajar con un buen entorno Django:

STATICFILES_DIRS=[os.path.join(os.path.expanduser("~/atom/django_api1/apptest"), "static")]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/username/folderProjects/projectname/media"
MEDIA_ROOT = os.path.join(os.path.expanduser("~/atom/django_api1"),"media")
# URL that handles the media served from MEDIA_ROOT. Make sure to use
# a trailing slash.
# Example: "http://example.com/media/"
MEDIA_URL = "/media/"
# Locale files translate language:
LOCALE_PATHS=(os.path.join(os.path.expanduser("~/atom/django_api1"),"locale"), )

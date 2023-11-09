from pathlib import Path
import os
from datetime import timedelta
from dotenv import load_dotenv
from decouple import config
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SITE_ID = config('SITE_ID')
REST_USE_JWT = config('REST_USE_JWT', default=False, cast=bool)

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # External Packages
    'rest_framework',
    'drf_spectacular',
    'djoser',
    'corsheaders',
    # Internal Apps
    'account',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    "corsheaders.middleware.CorsMiddleware",

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djoserauthapi.urls'

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

WSGI_APPLICATION = 'djoserauthapi.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : config('DB_NAME'),
        'USER' : config('DB_USER'),
        'PASSWORD' : config('DB_PASSWORD'),
        'HOST' : config('DB_HOST'),
        'PORT' : config('DB_PORT'),
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'account.User'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "UPDATE_LAST_LOGIN": False,
}

DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE':True,
    'ACTIVATION_URL':'/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL':True,
    'SEND_CONFIRMATION_EMAIL':True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION':True,
    'PASSWORD_RESET_CONFIRM_URL': 'password-reset/{uid}/{token}',
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'TOKEN_MODEL': None,# To Delete User Must Set it to None
    'SERIALIZERS':{
        'user_create': 'account.serializers.UserCreateSerializer',
        'user': 'account.serializers.UserCreateSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    },
    'EMAIL': {
        'activation': 'account.email.ActivationEmail',
        'confirmation': 'account.email.ConfirmationEmail',
        'password_reset': 'account.email.PasswordResetEmail',
        'password_changed_confirmation': 'account.email.PasswordChangedConfirmationEmail',
    },
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:3000',
]

EMAIL_BACKEND=config('EMAIL_BACKEND')
EMAIL_HOST=config('EMAIL_HOST')
EMAIL_PORT=config('EMAIL_PORT')
EMAIL_HOST_USER=config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=config('EMAIL_USE_TLS')


SPECTACULAR_SETTINGS = {

    'TITLE': 'Djoser Auth API',
    'DESCRIPTION': 'Djoser Auth API',
    'VERSION': '1.0.0',
    'SERVE_URLCONF': 'djoserauthapi.urls',
    'SCHEMA_PATH_PREFIX': r'/api/v1/',
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
    },
    'DEFAULT_GENERATOR_CLASS': 'drf_spectacular.generators.SchemaGenerator',
    'COMPONENT_SPLIT_REQUEST': True,
    'COMPONENT_SPLIT_RESPONSE': True,
    'COMPONENT_SPLIT_ENDPOINTS': True,
    'COMPONENTS': {
        'schemas': {
            'UserCreateSerializer': {
                'type': 'object',
                'properties': {
                    'email': {
                        'type': 'string',
                        'format': 'email',
                        'example': ''
                    },
                    'username': {
                        'type': 'string',
                        'example': 'user1',
                    },
                    'password': {
                        'type': 'string',
                        'example': 'password123',
                    },
                    're_password': {
                        'type': 'string',
                        'example': 'password123',
                    },
                },  
            },
            'UserSerializer': {
                'type': 'object',
                'properties': {
                    'id': {
                        'type': 'integer',
                        'example': 1,
                    },
                    'email': {
                        'type': 'string',
                        'format': 'email',
                        'example': ''           
                    },
                    'username': {
                        'type': 'string',
                        'example': 'user1',
                    },
                    'first_name': {
                        'type': 'string',
                        'example': 'John',
                    },
                    'last_name': {
                        'type': 'string',
                        'example': 'Doe',
                    },
                    'is_active': {
                        'type': 'boolean',
                        'example': True,
                    },
                    'is_staff': {
                        'type': 'boolean',
                        'example': False,
                    },
                    'is_superuser': {
                        'type': 'boolean',
                        'example': False,
                    },
                    'last_login': {
                        'type': 'string',
                        'format': 'date-time',
                        'example': '2021-05-06T11:38:00Z',
                    },
                    'date_joined': {
                        'type': 'string',
                        'format': 'date-time',
                        'example': '2021-05-06T11:38:00Z',
                    },
                },
            },
            'UserDeleteSerializer': {
                'type': 'object',
                'properties': {
                    'password': {
                        'type': 'string',
                        'example': 'password123',
                    },
                },
            },
            'UserChangePasswordSerializer': {
                'type': 'object',
                'properties': {
                    'old_password': {
                        'type': 'string',
                        'example': 'password123',
                    },
                    'new_password': {
                        'type': 'string',
                        'example': 'password123',
                    },
                    're_new_password': {
                        'type': 'string',
                        'example': 'password123',
                    },
                },
            },
            'UserResetPasswordSerializer': {
                'type': 'object',
                'properties': {
                    'new_password': {
                        'type': 'string',
                        'example': 'password123',
                    },
                    're_new_password': {
                        'type': 'string',
                        'example': 'password123',
                    },
                },
            },
            'UserResetPasswordConfirmSerializer': {
                'type': 'object',
                'properties': {
                    'new_password': {
                        'type': 'string',
                        'example': 'password123',
                    },
                    're_new_password': {
                        'type': 'string',
                        'example': 'password123',
                    },
                },
            },
            'UserResetPasswordConfirmSerializer': {
                'type': 'object',
                'properties': {
                    'new_password': {
                        'type': 'string',
                        'example': 'password123',
                    },
                    're_new_password': {
                        'type': 'string',
                        'example': 'password123',
                    },
                },
            },
            'UserResetPasswordConfirmSerializer': {
                'type': 'object',
                'properties': {
                    'new_password': {
                        'type': 'string',
                        'example': 'password123',
                    },
                    're_new_password': {
                        'type': 'string',
                        'example': 'password123',
                    },
                },
            },
            'UserResetPasswordConfirmSerializer': {
                'type': 'object',
                'properties': {
                    'new_password': {
                        'type': 'string',
                        'example': 'password123',
                    },
                    're_new_password': {
                        'type': 'string',
                        'example': 'password123',
                    },
                },
            },
            'UserResetPasswordConfirmSerializer': {
                'type': 'object',
                'properties': {
                    'new_password': {
                        'type': 'string',
                        'example': 'password123',
                    },
                    're_new_password': {
                        'type': 'string',
                        'example': 'password123',
                    },
                },
            },
        },
    },
}



import os

ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# '-05sgp9!deq=q1nltm@^^2cc+v29i(tyybv3v2t77qi66czazj'

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# my installed apps
INSTALLED_APPS += [
    'core.apps.CoreConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'demo.urls'

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_files')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if os.environ.get('DATABASE') == 'MYSQL':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT'),
        }
    }
elif os.environ.get('DATABASE') == 'POSTGRESQL':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT'),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, 'db.sqlite3')
        }
    }
ENVIRONMENT = os.environ.get('ENVIRONMENT')

if ENVIRONMENT == 'production':
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #SESSION_COOKIE_SECURE = True
    #SECURE_BROWSER_XSS_FILTER = True
    #SECURE_CONTENT_TYPE_NOSNIFF = True
    #SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    #SECURE_HSTS_SECONDS = 31536000
    #SECURE_REDIRECT_EXEMPT = []
    #SECURE_SSL_REDIRECT = True
    #SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
else:
    DEBUG = True
    SECRET_KEY = '123456789)*(&^%$#@'

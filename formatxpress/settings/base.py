from pathlib import Path
from os.path import join
from utils.constants import Settings, EmailConfig
from django.utils.timezone import timedelta
from dotenv import dotenv_values

env = dotenv_values(".env")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Auth User Model
AUTH_USER_MODEL = Settings.AUTH_USER_MODEL
APPEND_SLASH = True

# SECURITY WARNING: keep the secret key used in production secret!
# -------------------------------------------------
SECRET_KEY = env.get("SECRET_KEY")
CITIES_LIGHT_INCLUDE_COUNTRIES = ["IN"]

# Application definition
# -------------------------------------------------
THIRD_PARTY_APPS = [
    "rest_framework",
    "django_extensions",
    "corsheaders",
    "cities_light",
    "rest_framework_simplejwt",
    "phonenumber_field",
    "django_rq",
]


PROJECT_APPS = [
    "accounts.apps.AccountsConfig",
    "html_pdf.apps.HtmlPdfConfig",
]
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
INSTALLED_APPS = THIRD_PARTY_APPS + PROJECT_APPS + DJANGO_APPS


# Middlewares
# -------------------------------------------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Root Urls
# -------------------------------------------------
ROOT_URLCONF = Settings.ROOT_URLCONF

# Templates + Context Processors
# -------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [join(BASE_DIR, Settings.TEMPLATES_URLS)],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI - Web Server Gateway Interface Server
# -------------------------------------------------
WSGI_APPLICATION = Settings.WSGI_APPLICATION

# existing code...
SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_COOKIE_NAME = "sessionid"

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
# -------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
# -------------------------------------------------
LANGUAGE_CODE = Settings.LANGUAGE_CODE
USE_TZ = True
LANGUAGES = [
    ("en", "English"),
    ("hi", "Hindi"),
]
LOCALE_PATHS = [
    join(BASE_DIR, "locale"),
]

TIME_ZONE = Settings.TIME_ZONE

USE_I18N = Settings.USE_I18N

USE_TZ = Settings.USE_TZ


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
# -------------------------------------------------
STATIC_URL = Settings.STATIC_URL
STATICFILES_DIRS = [join(BASE_DIR, Settings.STATIC_FILES_DIRS)]
STATIC_ROOT = join(BASE_DIR, Settings.STATIC_ROOT)

# Media files (Models File)
# -------------------------------------------------
MEDIA_URL = Settings.MEDIA_URL
MEDIA_ROOT = join(BASE_DIR, Settings.MEDIA_ROOT)


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
# -------------------------------------------------
DEFAULT_AUTO_FIELD = Settings.DEFAULT_AUTO_FIELD

# Email Configuration
# =====================================================
EMAIL_BACKEND = EmailConfig.EMAIL_BACKEND
EMAIL_HOST = EmailConfig.EMAIL_HOST
EMAIL_USE_SSL = True  # use port 465
EMAIL_USE_TLS = False  # use port 587
EMAIL_PORT = EmailConfig.PORT_465 if EMAIL_USE_SSL else EmailConfig.PORT_587
EMAIL_HOST_USER = env.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env.get("EMAIL_HOST_PASSWORD")

# Rest Framework Configuration
# https://www.django-rest-framework.org/
REST_FRAMEWORK = {
    # "DEFAULT_PERMISSION_CLASSES": [
    #     "rest_framework.permissions.IsAuthenticated",
    # ],
    "DEFAULT_FILTER_BACKENDS": [
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=7),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=28),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}

# Redis Queue Configurations
RQ_QUEUES = {
    "default": {
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
    },
    "high": {
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
    },
    "low": {
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
    },
}

# Logging Configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} - {asctime} - {name} - {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "debug.log",
            "formatter": "verbose",
        },
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "INFO",
    },
}

# Cache Configuration
# =====================================================
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": BASE_DIR / "cache",
    }
}

from django.utils.translation import gettext_lazy as _

DD_MM_YYYY = "%d-%m-%Y"
YYYY_MM_DD = "%Y-%m-%d"


class Templates:
    """Default Templates Constants"""

    SUCCESS_TEMPLATE = "api/success.html"
    ERROR_TEMPLATE = "api/error.html"


class Settings:
    """Default Settings Constants"""

    ROOT_URLCONF = "conf.urls"
    AUTH_USER_MODEL = "accounts.User"
    WSGI_APPLICATION = "conf.wsgi.application"
    ASGI_APPLICATION = "conf.asgi.application"
    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "Asia/Kolkata"
    USE_I18N = True
    USE_TZ = True
    STATIC_URL = "static/"
    STATIC_ROOT = "assets/"
    STATIC_FILES_DIRS = "static/"
    TEMPLATES_URLS = "templates/"
    MEDIA_URL = "media/"
    MEDIA_ROOT = "media/"
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


class EmailConfig:
    """Email Constants"""

    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    PORT_465 = 465
    PORT_587 = 587


class CacheTimeout:
    """Cache Timeout Constants"""

    ONE_MINUTE = 60
    TEN_MINUTES = 60 * 10
    THIRTY_MINUTES = 60 * 30
    ONE_HOUR = 60 * 60
    ONE_DAY = 60 * 60 * 24
    ONE_WEEK = 60 * 60 * 24 * 7

    @classmethod
    def x_minutes(cls, x: int):
        return x * 60

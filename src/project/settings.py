from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

from env_settings import EnvSettings

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent
ENV = EnvSettings()

SECRET_KEY = ENV.DJ.SECRET_KEY

DEBUG = ENV.DJ.DEBUG

ALLOWED_HOSTS = ENV.DJ.ALLOWED_HOSTS

CSRF_TRUSTED_ORIGINS = ENV.DJ.CSRF_TRUSTED_ORIGINS

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Libraries
    "rest_framework",
    "django_filters",
    "drf_yasg",
    # Apps
    "course",
    "user",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "project.wsgi.application"

AUTH_USER_MODEL = "user.User"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": ENV.POSTGRES_DSN.path[1:],
        "USER": ENV.POSTGRES_DSN.user,
        "PASSWORD": ENV.POSTGRES_DSN.password,
        "HOST": ENV.POSTGRES_DSN.host,
        "PORT": ENV.POSTGRES_DSN.port,
        "ATOMIC_REQUESTS": True,
    },
}

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

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "common.page_size.CustomPageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.DjangoModelPermissions",
    ),
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.MultiPartParser",
    ),
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_THROTTLE_RATES": {"anon": "10/second", "user": "50/second"},
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",
    "DATE_FORMAT": "%Y-%m-%d",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Asia/Qyzylorda"

USE_I18N = True

USE_TZ = False

STATIC_URL = ENV.DJ.STATIC_URL

STATIC_ROOT = "/collected_static"

MEDIA_URL = ENV.DJ.MEDIA_URL
MEDIA_ROOT = "/media"
STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

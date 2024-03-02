import os
from pathlib import Path
import dj_database_url
# from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$epx^r=3u8b8pt+yc_3&e)50gr1%-@3jgpl#j-&9&am#$2on*8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['tanabeles.com','www.tanabeles.com', '146.190.142.200','localhost']

# Appication definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'category.apps.CategoryConfig',
    'store.apps.StoreConfig',
    'carts.apps.CartsConfig',
    'orders.apps.OrdersConfig',
    'nested_admin',
    'tailwind',
    'theme',
    'django_quill',
    # 'django_browser_reload',
    'footer.apps.FooterConfig',
    'heads.apps.HeadsConfig',
    'blog.apps.BlogConfig', 
    'contact.apps.ContactConfig',
    'advertizement.apps.AdvertizementConfig',
    # 'crispy_forms',


     'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]
# CRISPY_TEMPLATE_PACK = 'tailwind'

ACCOUNT_EMAIL_VERIFICATION = 'none'  # Email verification turned off for simplicity
LOGIN_REDIRECT_URL = '/'  # Redirect to home after login
SOCIALACCOUNT_QUERY_EMAIL = True  # Set to True to get email from social account providers


TAILWIND_APP_NAME = 'theme'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # "django_browser_reload.middleware.BrowserReloadMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'msigana_ecommerce.urls'

INTERNAL_IPS = [
    "127.0.0.1",
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processors.menu_links',
                'carts.context_processors.counter', 
                'footer.context_processors.footer',
                'heads.context_processors.head_contents',
                'store.context_processors.most_liked_products',
                'advertizement.context_processors.advertizement_first',
                'advertizement.context_processors.advertizement_second',
                'advertizement.context_processors.advertizement_third',
                'advertizement.context_processors.favicon',
                'users.context_processors.liked_products',

            ],
        },
    },
]

WSGI_APPLICATION = 'msigana_ecommerce.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# if  DEBUG:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': 'ecommerce_postgres',
#             'USER': 'postgres',
#             'PASSWORD': 'Melaku11@#',
#             'HOST': 'localhost',
#             'PORT': '5432',
#         }
#     }
# else:
DATABASES = {
        'default': dj_database_url.parse('postgresql://doadmin:AVNS_Hb9Nhg89MYv_2-SoBeS@tanabeles-one-do-user-15632631-0.c.db.ondigitalocean.com:25060/defaultdb?sslmode=require')
    }



    
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'my_cache_table',
#     }
# }


AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
    
]

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.CustomUser'

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '853190814013-ufc76ofqcv2lj72i5l8rehpa03tp3gk7.apps.googleusercontent.com',
            'secret': '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',
        }
    },
    'facebook': {
        'APP': {
            'client_id': '378221998142570',
            'secret': '3d9b77b8daad0a6686ff0713ec7b3cd5',
        }
    }
}
ACCOUNT_FORMS = {'signup': 'users.forms.CustomSignupForm'}

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'


SOCIALACCOUNT_ADAPTER = 'users.adapters.account_adapter.CustomSocialAccountAdapter'

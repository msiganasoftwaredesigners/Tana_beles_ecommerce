import os
from pathlib import Path
from decouple import  config


BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = config('DEBUG', default=False, cast=bool)


ACCOUNT_EMAIL_VERIFICATION = 'none'  
LOGIN_REDIRECT_URL = '/'  
SOCIALACCOUNT_QUERY_EMAIL = True  


TAILWIND_APP_NAME = 'theme'


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


    

AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
    
]


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'


STATICFILES_DIRS = [
    BASE_DIR / '../static',
]

STATIC_ROOT = BASE_DIR / '../staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / '../media'


# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.CustomUser'


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': config('GOOGLE_CLIENT_ID'),
            'secret': config('GOOGLE_SECRET'),
        }
    },
    'facebook': {
        'APP': {

            'client_id': config('FACEBOOK_CLIENT_ID'),
            'secret': config('FACEBOOK_SECRET'),
        }
    }
}

ACCOUNT_FORMS = {'signup': 'users.forms.CustomSignupForm'}

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'


SOCIALACCOUNT_ADAPTER = 'users.adapters.account_adapter.CustomSocialAccountAdapter'

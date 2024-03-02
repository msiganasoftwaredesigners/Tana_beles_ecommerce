# msigana_ecommerce/settings/dev.py

from .base import *
from decouple import  config


DEBUG = True

SECRET_KEY = config('SECRET_KEY')


ALLOWED_HOSTS = [config('ALLOWED_HOSTS_DEV')]


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
    'django_browser_reload',
    'footer.apps.FooterConfig',
    'heads.apps.HeadsConfig',
    'blog.apps.BlogConfig', 
    'contact.apps.ContactConfig',
    'advertizement.apps.AdvertizementConfig',
  
     'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DEV_DATABASE_NAME'),
        'USER': config('DEV_DATABASE_USER'),
        'PASSWORD': config('DEV_DATABASE_PASSWORD'),
        'HOST': config('DEV_DATABASE_HOST', default='localhost'),
        'PORT': config('DEV_DATABASE_PORT', default='5432'),
    }
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


STATIC_URL = '/static/'
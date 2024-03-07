from .base import *
from decouple import  config

DEBUG = True


SECRET_KEY = config('SECRET_KEY')


ALLOWED_HOSTS = config('ALLOWED_HOSTS_PROD').split(',')




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'users.apps.UsersConfig',
    'category.apps.CategoryConfig',
    'store.apps.StoreConfig',
    'carts.apps.CartsConfig',
    'orders.apps.OrdersConfig',
    'footer.apps.FooterConfig',
    'advertizement.apps.AdvertizementConfig',
    'contact.apps.ContactConfig',
    'blog.apps.BlogConfig', 
    'heads.apps.HeadsConfig',
    'telebirrpay.apps.TelebirrpayConfig',
    'nested_admin',
    'tailwind',
    'theme',
    'django_quill',
  
     'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('PROD_DATABASE_NAME'),
        'USER': config('PROD_DATABASE_USER'),
        'PASSWORD': config('PROD_DATABASE_PASSWORD'),
        'HOST': config('PROD_DATABASE_HOST'),
        'PORT': config('PROD_DATABASE_PORT'),
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    'https://tanabeles.com',
    'tanabeles.com',
    'https://www.tanabeles.com',
    'http://64.23.192.127',
    'http://localhost:8000',
    'http://localhost',
    '24.199.76.86',
]


# # HTTPS settings
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True


# # HSTS settings
# SECURE_HSTS_SECONDS = 31536000 # 1 year
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True


# # ??
# SECURE_BROWSER_XSS_FILTER = True


# CSRF_COOKIE_HTTPONLY = True



# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


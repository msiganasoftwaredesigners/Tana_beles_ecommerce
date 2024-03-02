import os

from django.core.asgi import get_asgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'msigana_ecommerce.settings.dev')

environment = os.environ.get('ENVIRONMENT', 'development')
settings_module = 'msigana_ecommerce.settings.dev' if environment == 'development' else 'msigana_ecommerce.settings.prod'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)


application = get_asgi_application()

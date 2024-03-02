import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'msigana_ecommerce.settings.dev')

# Determine the environment based on the ENVIRONMENT environment variable
environment = os.environ.get('ENVIRONMENT', 'development')
settings_module = 'msigana_ecommerce.settings.dev' if environment == 'development' else 'msigana_ecommerce.settings.prod'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()



import os



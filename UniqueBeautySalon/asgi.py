"""
ASGI config for UniqueBeautySalon project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UniqueBeautySalon.settings')

application = get_asgi_application()
LOGIN_REDIRECT_URL = 'home'  # after login
LOGOUT_REDIRECT_URL = 'login'  # after logout
LOGIN_URL = 'login'
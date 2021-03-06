"""
WSGI config for movies_recomm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movies_recomm.settings")

application = get_wsgi_application()

print(application)
application = WhiteNoise(application)
print(application)
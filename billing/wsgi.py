"""
WSGI config for billing project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restrack.settings")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

from dj_static import Cling

application = get_wsgi_application()
application = Cling(get_wsgi_application())
application = DjangoWhiteNoise(application)
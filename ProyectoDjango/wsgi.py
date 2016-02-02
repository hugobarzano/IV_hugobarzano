"""
WSGI config for ProyectoDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
#from dj_static import Cling

#Despliegue en PaaS



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProyectoDjango.settings")
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
#application = DjangoWhiteNoise(application)
#application = Cling(get_wsgi_application())

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

from dj_static import Cling

#Despliegue en PaaS
ON_OPENSHIFT = os.environ.get('OPENSHIFT_POSTGRESQL_PORT')
if ON_OPENSHIFT:
	virtenv = os.environ['APPDIR'] + '/virtenv/'
	os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.6/site-packages')
	virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
	try:
    		execfile(virtualenv, dict(__file__=virtualenv))
	except:
    		pass

	os.environ['DJANGO_SETTINGS_MODULE'] = os.environ['OPENSHIFT_APP_NAME']+'.settings'
	sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', os.environ['OPENSHIFT_APP_NAME']))
	application = django.core.handlers.wsgi.WSGIHandler()

else:
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProyectoDjango.settings")
	application = get_wsgi_application()
	application = Cling(get_wsgi_application())


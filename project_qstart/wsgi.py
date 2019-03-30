"""
WSGI config for project_qstart project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
from conf import config
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', str(
    config.get('project_settings', 'project_qstart.settings')))

application = get_wsgi_application()

"""
WSGI config for talkLims project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

path = '/var/www/talkLims'
if path not in sys.path:
    sys.path.append(path)

path = '/var/www/talkLims/talkLims'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "talkLims.settings")

application = get_wsgi_application()

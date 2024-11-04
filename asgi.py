"""
ASGI config for bca_majorproject_live_examinations_applications project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bca_majorproject_live_examinations_applications.settings')

application = get_asgi_application()

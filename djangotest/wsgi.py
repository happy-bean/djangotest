"""
WSGI config for djangotest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""
#一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangotest.settings")

application = get_wsgi_application()

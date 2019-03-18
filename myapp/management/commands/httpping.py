from django.core.management import BaseCommand
import socket
from django.conf import settings
import requests as req

from myapp.models import SqlServer, SqlLog, WebApplication


def update_status(webapp, online):
    webapp.online = online
    webapp.save()


def log_event(webapp):
    s = set()
    s.add(webapp)
    log = SqlLog.objects.create()
    log.title = 'Down: %s' % webapp.name
    log.servers.set(s)
    log.save()


def http_ping(webapp):
    try:
        r = req.get(webapp.url, timeout=20)
        update_status(webapp, True)
        if settings.DEBUG:
            print('%s is listening on port %s' % (webapp, webapp.port))
    except e:
        log_event(webapp)
        update_status(webapp, False)
    finally:
        s.close()


class Command(BaseCommand):
    help = 'Ping all of the Web applications with monitor=True'

    def handle(self, *args, **options):
        webapps = WebApplication.objects.all()

        [http_ping(webapp) for webapp in webapps if webapp.monitor]

from django.core.management import BaseCommand
from datetime import datetime
import socket

from myapp.models import SqlServer, SqlLog


def log_event(sqlserver):
    s = set()
    s.add(sqlserver)
    log = SqlLog.objects.create()
    log.title = 'Down: %s' % sqlserver.name
    log.servers.set(s)
    log.save()


def sql_ping(sqlserver):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((sqlserver.name, sqlserver.port))
        print('%s is listening on port %s' % (sqlserver, sqlserver.port))
    except socket.error:
        log_event(sqlserver)
    finally:
        s.close()


class Command(BaseCommand):
    help = 'Ping all of the SQL Servers with monitor=True'

    def handle(self, *args, **options):
        sqlservers = SqlServer.objects.all()
        self.stdout.write('SQL Servers: %s' % sqlservers.count())
        for sqlserver in sqlservers:
            if sqlserver.monitor: sql_ping(sqlserver)

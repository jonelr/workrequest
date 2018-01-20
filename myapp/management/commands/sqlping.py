from django.core.management import BaseCommand
import socket

from myapp.models import SqlServer

PORT = 1433


def sql_ping(sqlserver):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((sqlserver, PORT))
        print('%s is listening on port %s' % (sqlserver, PORT))
    except socket.error:
        pass
    finally:
        s.close()


class Command(BaseCommand):
    help = 'Ping all of the SQL Servers with monitor=True'

    def handle(self, *args, **options):
        sqlservers = SqlServer.objects.all()
        self.stdout.write('SQL Servers: %s' % sqlservers.count())
        for sqlserver in sqlservers:
            sql_ping(sqlserver.name)

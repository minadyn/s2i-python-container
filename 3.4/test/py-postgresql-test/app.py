import os
import postgresql

from gunicorn.app.base import BaseApplication
from gunicorn.six import iteritems


def wsgi_handler(environ, start_response):
    db = postgresql.open(os.environ['PG_CONN_STR'])
    start_response('200 OK', [('Content-Type','text/html')])
    return [str.encode("Hello World from standalone WSGI application! You are using postgres: %s" % (db.version,))]

class StandaloneApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

if __name__ == '__main__':
    StandaloneApplication(wsgi_handler, {'bind': ':8080'}).run()

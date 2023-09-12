# This module is separated from application.py to make db.Model import to
# actually create tables in db.metadata. If create_application() is called from
# inside application.py the 'magic' db.Model addition to db.metadata fails to
# create tables in the metadata (in the correct db instance).

from application import create_application


def run_application():
    '''Run application in dev mode. No WSGI.'''
    app = create_application()
    app.run(port=8080)


if __name__ == '__main__':
    run_application()

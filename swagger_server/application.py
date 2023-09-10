#!/usr/bin/env python3

import os

import connexion
import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy

from encoder import JSONEncoder


db = SQLAlchemy()


def create_application():
    app = connexion.App(__name__, specification_dir='./swagger/')

    # This seems to be needed by connexion
    app.app.json_encoder = JSONEncoder

    # Enable API 'mode' of connexion
    app.add_api('swagger.yaml', arguments={'title': 'Simple Anagram API'},
                pythonic_params=True, validate_responses=True)

    # Configure the Flask application
    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.app.config.from_object(config_type)
    app.app.logger.info(f'Reading config {config_type} done...')

    # Initialize DB
    db.init_app(app.app)
    # Check if the DB schema needs to be initialized
    from models.corpus import Corpus

    engine = sa.create_engine(app.app.config['SQLALCHEMY_DATABASE_URI'])
    inspector = sa.inspect(engine)
    if not inspector.has_table("corpus"):
        with app.app.app_context():
            db.drop_all()
            db.create_all()
            app.app.logger.info('Database initialization done...')
    else:
        app.app.logger.info('Database already initialized - skipping initialization')

    return app

def run_application():
    '''Run application in dev mode. No WSGT.'''
    app = create_application()
    app.run(port=8080)


if __name__ == '__main__':
    run_application()

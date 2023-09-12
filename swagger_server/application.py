#!/usr/bin/env python3

import os

import connexion
import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy
from connexion.apps.flask_app import FlaskJSONEncoder


db = SQLAlchemy()


def create_application():
    connexion_app = connexion.App(__name__, specification_dir='./swagger/')

    # This seems to be needed by connexion
    connexion_app.json_encoder = FlaskJSONEncoder
    flask_app = connexion_app.app

    # Enable API 'mode' of connexion
    connexion_app.add_api('swagger.yaml', arguments={'title': 'Simple Anagram API'},
                          pythonic_params=True, validate_responses=True)

    # Configure the Flask application
    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    flask_app.config.from_object(config_type)
    flask_app.logger.info(f'Reading config {config_type} done...')

    # Initialize DB
    db.init_app(flask_app)
    # Check if the DB schema needs to be initialized
    from models.corpus import Corpus

    engine = sa.create_engine(flask_app.config['SQLALCHEMY_DATABASE_URI'])
    inspector = sa.inspect(engine)
    if not inspector.has_table('corpus'):
        with flask_app.app_context():
            db.drop_all()
            db.create_all()

            flask_app.logger.info('Database initialization done...')
    else:
        flask_app.logger.info('Database already initialized - skipping initialization')

    return connexion_app


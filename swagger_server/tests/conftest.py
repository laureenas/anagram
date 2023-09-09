import pytest

from application import create_application


@pytest.fixture(scope='module')
def app():
    '''Set the Testing configuration prior to creating the Flask application'''

    connextion_app = create_application()
    flask_app = connextion_app.app

    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app


@pytest.fixture(scope='module')
def client(app):
    '''A client for executing calls'''
    with app.test_client() as test_client:
        # Establish an application context
        with app.app_context():
            yield test_client

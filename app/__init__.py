from flask import Flask
import mimetypes
from instance.config import app_config


def create_app(config_name='development'):

    app = Flask(__name__, instance_relative_config=True, static_url_path='', static_folder='static')

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024
    mimetypes.add_type('application/javascript', '.js')
    mimetypes.add_type('text/css', '.css')

    from app.api.v1 import blueprint_v1  # noqa

    app.register_blueprint(blueprint_v1, url_prefix='/api/')

    return app

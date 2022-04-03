import logging

from flask import Flask
from flask_restful import Api
from waitress import serve

from views.views import Health
import settings


def create_app():
    app = Flask(__name__)
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app


logging.basicConfig(format=settings.LOG_PATTERN, level=logging.INFO)

app = create_app()
app_context = app.app_context()
app_context.push()

api = Api(app)
api.add_resource(Health, '/health')


if __name__ == "__main__":
    logging.info(f'{settings.APP} Server started')
    serve(
        app=app,
        host='0.0.0.0',
        port=8000,
        threads=settings.WAITRESS_WORKERS,
        connection_limit=settings.WAITRESS_CHANNELS,
    )

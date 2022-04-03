import os
import datetime as dt

from werkzeug.security import generate_password_hash

# APP
APP = 'black-list-email'
APP_VERSION = "0.1.0"
DEFAULT_TIMEOUT = int(os.getenv('DEFAULT_TIMEOUT', 4))
DEPLOYED_AT = dt.datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
DEBUG = os.getenv('DEBUG', False)
LOG_PATTERN = '%(asctime)s.%(msecs)s:%(name)s:%(thread)d:(%(threadName)-10s)' \
              ':%(levelname)s:%(process)d:%(message)s'

# security
basic_auth_password_ms = os.getenv("basic_auth_password_ms", "123")
basic_auth_users = {
    "ms": generate_password_hash(basic_auth_password_ms),
}

# Config Local Database
DB_MICROSERVICE_HOST = \
    os.getenv('db_host', 'localhost')
DB_MICROSERVICE_PORT = \
    int(os.getenv('db_port', 5432))
DB_MICROSERVICE_USERNAME = \
    os.getenv('db_user', 'postgres')
DB_MICROSERVICE_PASSWORD = \
    os.getenv('db_password', 'postgres')
DB_MICROSERVICE_DATABASE = \
    os.getenv('db_name', 'postgres')

# WAITRESS CONFIG
WAITRESS_WORKERS = int(os.getenv('WAITRESS_WORKERS', 8))
WAITRESS_CHANNELS = int(os.getenv('WAITRESS_CHANNELS', 100))

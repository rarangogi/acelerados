from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import settings

postgres_uri = "postgresql+psycopg2://{username}:{password}@{host}:" \
               "{port}/{db}".format(
                username=settings.DB_MICROSERVICE_USERNAME,
                password=settings.DB_MICROSERVICE_PASSWORD,
                host=settings.DB_MICROSERVICE_HOST,
                port=settings.DB_MICROSERVICE_PORT,
                db=settings.DB_MICROSERVICE_DATABASE
                )

engine = create_engine(postgres_uri, pool_pre_ping=True)

# Declaring the mapping
Base = declarative_base()


def create_session(engine_object: object):
    session_factory = scoped_session(sessionmaker(bind=engine_object))

    return session_factory

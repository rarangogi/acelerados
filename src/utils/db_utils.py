import logging
import traceback

from sqlalchemy.orm.session import Session
from settings import APP


def save_to_db(session: Session, db_model: object) -> None:
    logging.info(f"{APP}: writing instance on {db_model}")
    try:
        session.add(db_model)
        session.commit()
    except Exception as err:
        logging.warning('ADD DB ERROR: error={0} trace={1}'.format(
            err, " ".join(traceback.format_exc().splitlines()))
        )
        session.rollback()


def update_db(session: Session, records: list) -> None:
    logging.info(f"{APP}: update instance on {records}")
    try:
        for record in records:
            session.merge(record)
        session.commit()
    except Exception as err:
        logging.warning('ADD DB ERROR: error={0} trace={1}'.format(
            err, " ".join(traceback.format_exc().splitlines()))
        )
        session.rollback()

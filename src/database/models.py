from datetime import datetime

from sqlalchemy import Column,  String, DateTime, BigInteger, TEXT

from database.db import Base


class BlackListModel(Base):
    __tablename__ = 'black_list'
    id = Column("id", BigInteger, primary_key=True, autoincrement=True)
    email = Column("email", String(50))
    app_uuid = Column("app_uuid", String(20))
    ip = Column("ip", String(20))
    blocked_reason = Column("blocked_reason", TEXT)
    created_at = Column("created_at", DateTime, default=datetime.utcnow)

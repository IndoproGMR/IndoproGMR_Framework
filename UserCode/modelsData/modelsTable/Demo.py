from sqlalchemy import Boolean, Column, ForeignKey, Index, Integer, String, Text
from sqlalchemy.orm import relationship

from APP.config.manager.sqlmanager import Base


class user_table(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(Text)
    umur = Column(Integer, index=True)
    hidup = Column(Integer, default=1)


class data_user_table(Base):
    __tablename__ = "data_user"

    id = Column(Integer, primary_key=True, autoincrement=True)

    id_user = Column(Integer)
    diskripsi = Column(Text)

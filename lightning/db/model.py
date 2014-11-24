# -*- coding: utf-8 -*- 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Enum, MetaData, ForeignKey, Unicode, Boolean, DateTime
from sqlalchemy.orm import relationship, backref

base = declarative_base()

class UserAuth(base):
    # Due to the authentication center doesn't provide an API, so we have to
    # type in the table here . After the authentication center is removed from
    # AllChat as a single model, the table will be useless here.
    # For the above reason, we don't add a __init__ function here.
    __tablename__ = "userauth"
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
        'mysql_collate': 'utf8_bin'
    }

    id = Column(Integer, primary_key = True)
    account = Column(String(50), index = True, unique = True, nullable = False)
    password = Column(String(64), nullable = False)
    salt = Column(String(16), nullable = False)
    prev_token = Column(String(32))
    token = Column(String(32))
    created = Column(DateTime(timezone = True), nullable = False)
    updated = Column(DateTime(timezone = True), nullable = False)
    deleted = Column(Boolean, nullable = False, default = False)
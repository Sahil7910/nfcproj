import mysql.connector
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Sequence, inspect, select
from sqlalchemy.orm import declarative_base


engine = create_engine("mysql://root:admin@localhost/nfcreader",echo = True)

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    password = Column(String(50))


class Members(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    cardid = Column(String(50))
    status  = Column(Integer)

conn = engine.connect()





# 'users', meta
# ins = users.insert()
# ins = users.insert().values(name = 'Ravi', password = 'Kapoor')






import sys 
import os
import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), '/'))

from sqlalchemy import create_engine, Column, Integer, DateTime
from db.base import Base
from db.load import engine

class LogPixCharge(Base):
    
    __tablename__ = 'pix_charge_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime)

    def __init__(self):
        self.date = datetime.datetime.now()


Base.metadata.create_all(engine)
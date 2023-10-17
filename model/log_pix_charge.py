import sys 
import os
import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), '/'))

from sqlalchemy import create_engine, Column, Integer, DateTime, String
from db.base import Base
from db.load import engine

class LogPixCharge(Base):
    
    __tablename__ = 'pix_charge_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime)
    address_requester = Column(String)
    def __init__(self, address_requester):
        self.date = datetime.datetime.now()
        self.address_requester = address_requester

Base.metadata.create_all(engine)
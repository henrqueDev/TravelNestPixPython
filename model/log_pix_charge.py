import sys 
import os
import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), '/'))

from sqlalchemy import Float, create_engine, Column, Integer, DateTime, String
from db.base import Base
from db.load import engine

class LogPixCharge(Base):
    
    __tablename__ = 'pix_charge_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime)
    id_user = Column(Integer)
    qnt_cob = Column(Float)
    id_hotel = Column(Integer)
    id_cob = Column(Integer)
    address_requester = Column(String)
    
    def __init__(self, address_requester, id_user, qnt_cob, id_hotel, id_cob):
        self.date = datetime.datetime.now()
        self.address_requester = address_requester
        self.id_user = id_user
        self.qnt_cob = qnt_cob
        self.id_hotel = id_hotel
        self.id_cob = id_cob

Base.metadata.create_all(engine)
import sys 
import os
import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), '/'))

from sqlalchemy import Date, Float, create_engine, Column, Integer, DateTime, String
from db.base import Base
from db.load import engine

class LogPixCharge(Base):
    
    __tablename__ = 'pix_charge_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime)
    id_user = Column(Integer)
    qnt_cob = Column(Float)
    id_hotel = Column(Integer)
    id_cob = Column(String)
    address_requester = Column(String)
    check_in = Column(Date)
    check_out = Column(Date)
    id_room_option = Column(Integer)
    pix_key = Column(String)

    def __init__(self, pix_key, address_requester, id_user, qnt_cob, id_hotel, id_cob, check_in, check_out, id_room_option):
        self.date = datetime.datetime.now()
        self.address_requester = address_requester
        self.id_user = id_user
        self.qnt_cob = qnt_cob
        self.id_hotel = id_hotel
        self.id_cob = id_cob
        self.check_in = check_in
        self.check_out = check_out
        self.id_room_option = id_room_option
        self.pix_key = pix_key
Base.metadata.create_all(engine)
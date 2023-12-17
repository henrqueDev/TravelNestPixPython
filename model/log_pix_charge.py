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
    user_id = Column(Integer)
    total_price = Column(Float)
    hotel_id = Column(Integer)
    cob_id = Column(String)
    address_requester = Column(String)
    check_in = Column(Date)
    check_out = Column(Date)
    room_option_id = Column(Integer)
    pix_key = Column(String)

    def __init__(self, pix_key, address_requester, user_id, total_price, hotel_id, cob_id, check_in, check_out, room_option_id):
        self.date = datetime.datetime.now()
        self.address_requester = address_requester
        self.user_id = user_id
        self.total_price = total_price
        self.hotel_id = hotel_id
        self.cob_id = cob_id
        self.check_in = check_in
        self.check_out = check_out
        self.room_option_id = room_option_id
        self.pix_key = pix_key
Base.metadata.create_all(engine)
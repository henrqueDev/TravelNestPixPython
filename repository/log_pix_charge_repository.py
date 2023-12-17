import sys 
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '/'))

from model.log_pix_charge import LogPixCharge 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.load import engine

class LogPixChargeRepository:

    def __init__(self):
        self.engine = engine
        self.session = sessionmaker(bind=self.engine)

    def save(self, pix_key, address_requester, user_id, total_price, hotel_id ,cob_id, check_in, check_out, room_option_id):
        pix_log = LogPixCharge(pix_key, address_requester, user_id, total_price, hotel_id ,cob_id, check_in, check_out, room_option_id)
        session = self.session()
        session.add(pix_log)
        session.commit()
        session.close()
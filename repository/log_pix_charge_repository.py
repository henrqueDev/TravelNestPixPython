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

    def save(self, pix_key, address_requester, id_user, qnt_cob, id_hotel ,id_cob, check_in, check_out, id_room_option):
        pix_log = LogPixCharge(pix_key, address_requester, id_user, qnt_cob, id_hotel ,id_cob, check_in, check_out, id_room_option)
        session = self.session()
        session.add(pix_log)
        session.commit()
        session.close()
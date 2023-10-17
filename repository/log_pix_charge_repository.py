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

    def save(self, address_requester):
        pix_log = LogPixCharge(address_requester)
        session = self.session()
        session.add(pix_log)
        session.commit()
        session.close()
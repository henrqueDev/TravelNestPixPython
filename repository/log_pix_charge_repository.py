import sys 
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '/'))

from model.log_pix_charge import LogPixCharge 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.load import engine

class LogPixChargeRepository:

    def __init__(self):
        self.__engine = engine
        self.__Session = sessionmaker(bind=self.__engine)

    def save(self):
        pix_log = LogPixCharge()
        session = self.__Session()
        session.add(pix_log)
        session.commit()
        session.close()
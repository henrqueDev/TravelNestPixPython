import sys 
import os

import injector
sys.path.append(os.path.join(os.path.dirname(__file__), '/'))

from model.log_pix_charge import LogPixCharge 
from sql_alchemy import banco

class LogPixChargeRepository:

    @injector
    def __init__(self, pix_charge_log_id , datetime):
        super(LogPixChargeRepository, self).__init__(LogPixCharge)
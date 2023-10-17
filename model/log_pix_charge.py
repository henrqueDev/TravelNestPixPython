import sys 
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '/'))

from sql_alchemy import banco

class LogPixCharge:
    
    __tablename__ = 'pix_charge_logs'

    pix_charge_log_id = banco.Column(banco.Integer, primary_key=True)
    date = banco.Column(banco.DateTime)

    def __init__(self, pix_charge_log_id , datetime):
        self.pix_charge_log_id = pix_charge_log_id
        self.date = datetime
# encoding: utf-8
import sys
import os

import requests

sys.path.append(os.path.join(os.path.dirname(__file__), '/'))

from efipay import EfiPay
import credentials
from repository.log_pix_charge_repository import LogPixChargeRepository


class PixCodeGenerator():
    
    def __init__(self):
        self.efi = EfiPay(credentials.CREDENTIALS)
        self.log_repository = LogPixChargeRepository()

    def generate_pix_code(self, pix_key, user_id, total_price, hotel_id, address_requester, check_in, check_out, room_option_id, children_quantity, adults_quantity):
        body = {
            'calendario': {
                'expiracao': 3600
            },
            'valor': {
                'original': "{:.2f}".format(float(total_price))
            },
            'chave': pix_key,
            'solicitacaoPagador': 'Cobrança dos serviços prestados.'
        }
        response =  self.efi.pix_create_immediate_charge(body=body)
        
        
        print(response)

        params = {
            'id': response['loc']['id']
        }
        response_code =  self.efi.pix_generate_qrcode(params=params) 
        
        requests.post("http://127.0.0.1:5000/consultaPagamentos", json={"pix_key": pix_key, "user_id": user_id, "hotel_id": hotel_id, "cob_id": response['txid'], 
                                                                        "total_price":  "{:.2f}".format(float(total_price)), "check_in": check_in, "check_out": check_out, "room_option_id": room_option_id, "status": response["status"],
                                                                          "children_quantity": children_quantity, "adults_quantity": adults_quantity  })
        self.log_repository.save(pix_key, address_requester, user_id, total_price, hotel_id, response['txid'],  check_in, check_out, room_option_id)
        return response_code['qrcode']

 
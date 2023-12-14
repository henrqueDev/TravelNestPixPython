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

    def generate_pix_code(self, pix_key, id_user, qnt_cob, id_hotel, address_requester, check_in, check_out, id_room_option):
        body = {
            'calendario': {
                'expiracao': 3600
            },
            'valor': {
                'original': "{:.2f}".format(float(qnt_cob))
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
        
        requests.post("http://127.0.0.1:5000/consultaPagamentos", json={"id_user": id_user, "id_hotel": id_hotel, "id_cob": response['txid'], 
                                                                        "qnt_cob":  "{:.2f}".format(float(qnt_cob)), "check_in": check_in, "check_out": check_out, "id_room_option": id_room_option, "status": response["status"]  })
        self.log_repository.save(pix_key, address_requester, id_user, qnt_cob, id_hotel, response['txid'],  check_in, check_out, id_room_option)
        return response_code['qrcode']

 
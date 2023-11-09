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

    def generate_pix_code(self, key, id_user, qnt_cob, id_hotel, address_requester):
        body = {
            'calendario': {
                'expiracao': 3600
            },
            'valor': {
                'original': qnt_cob
            },
            'chave': key,
            'solicitacaoPagador': 'Cobrança dos serviços prestados.'
        }

        response =  self.efi.pix_create_immediate_charge(body=body)
        #print(response)
        params = {
            'id': response['loc']['id']
        }
        
        response_code =  self.efi.pix_generate_qrcode(params=params)
        
        requests.post("http://127.0.0.1:5000/consultaPagamentos", json={"id_user": id_user, "id_hotel": id_hotel, "id_cob": response['loc']['id'], "qnt_cob": qnt_cob  })
        self.log_repository.save(address_requester, id_user, qnt_cob, id_hotel , response['loc']['id'])
        return response_code['qrcode']


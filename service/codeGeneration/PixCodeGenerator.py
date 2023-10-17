# encoding: utf-8
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '/'))

from efipay import EfiPay
import credentials
from repository.log_pix_charge_repository import LogPixChargeRepository


class PixCodeGenerator():
    
    def __init__(self):
        self.efi = EfiPay(credentials.CREDENTIALS)
        self.log_repository = LogPixChargeRepository()

    def generate_pix_code(self, key, value, address_requester):
        body = {
            'calendario': {
                'expiracao': 3600
            },
            'valor': {
                'original': value
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
        self.log_repository.save(address_requester)
        return response_code['qrcode']


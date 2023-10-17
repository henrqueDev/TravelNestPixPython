# encoding: utf-8

from efipay import EfiPay
import credentials


class PixCodeGenerator():
    
    def __init__(self):
        self.efi = EfiPay(credentials.CREDENTIALS)

    def generate_pix(self, chave, valor):
        body = {
            'calendario': {
                'expiracao': 3600
            },
            'valor': {
                'original': valor
            },
            'chave': chave,
            'solicitacaoPagador': 'Cobrança dos serviços prestados.'
        }

        response =  self.efi.pix_create_immediate_charge(body=body)


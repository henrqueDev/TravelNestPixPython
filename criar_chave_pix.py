# encoding: utf-8

from efipay import EfiPay
import credentials

efi = EfiPay(credentials.CREDENTIALS)

response =  efi.pix_create_evp()
print(response)


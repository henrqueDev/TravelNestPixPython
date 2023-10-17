# encoding: utf-8
import os
from dotenv import load_dotenv

load_dotenv()
# Insira aqui suas credenciais
CREDENTIALS = {
    'client_id': os.getenv('CLIENT_ID') ,
    'client_secret': os.getenv('CLIENT_SECRET'),
    'sandbox':  False, # True: Ambiente de Homologação |  False: Ambiente de Produção
    'certificate': os.getenv('CERTIFICATE_PATH')
}
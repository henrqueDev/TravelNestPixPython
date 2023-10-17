import unittest
from unittest.mock import Mock
from efipay import EfiPay

import sys 
import os
import credentials

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))

from model.log_pix_charge import LogPixCharge
from service.codeGeneration.PixCodeGenerator import PixCodeGenerator
from db.load import engine

class TestPixCodeGenerator(unittest.TestCase):

    def test_init(self):
        pix_code_generator = PixCodeGenerator()

        self.assertIsNotNone(pix_code_generator.efi)
        self.assertIsNotNone(pix_code_generator.log_repository)

import unittest
from unittest.mock import Mock
import sys 
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from model.log_pix_charge import LogPixCharge

class TestLogPixCharge(unittest.TestCase):

    def test_init(self):
        address_requester = "test_address"
        log_pix_charge = LogPixCharge(address_requester)

        self.assertEqual(log_pix_charge.address_requester, address_requester)
        self.assertIsNotNone(log_pix_charge.date)

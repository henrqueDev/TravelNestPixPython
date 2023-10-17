import unittest
from unittest.mock import Mock

import sys 
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from model.log_pix_charge import LogPixCharge
from repository.log_pix_charge_repository import LogPixChargeRepository
from db.load import engine

class TestLogPixChargeRepository(unittest.TestCase):

    def test_init(self):
        log_pix_charge_repository = LogPixChargeRepository()

        self.assertEqual(log_pix_charge_repository.engine, engine)
        self.assertIsNotNone(log_pix_charge_repository.session)


from unittest.mock import MagicMock
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '/'))

from service.codeGeneration import genqrcode_pb2, genqrcode_pb2_grpc
from service.codeGeneration.PixCodeGenerator import PixCodeGenerator

class TestGenerator:
    def test_generate(self):
        request = MagicMock()
        context = MagicMock()
        request.return_value = None
        response = None

        assert response.res is not None
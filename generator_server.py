# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '/'))


from concurrent import futures
import logging

import grpc

from service.qrCodeGeneration import genqrcode_pb2, genqrcode_pb2_grpc
from service.qrCodeGeneration.PixCodeGenerator import PixCodeGenerator
import db.load

class Generator(genqrcode_pb2_grpc.GenQrCodeServiceServicer):
    def Generate(self, request, context):
        gen = PixCodeGenerator()
        code = gen.generate_pix_code("1e84d92a-8997-41cc-9ca6-331cc602e857", "0.01")
        return genqrcode_pb2.responseCode(res="%s" % code)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    genqrcode_pb2_grpc.add_GenQrCodeServiceServicer_to_server(Generator(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

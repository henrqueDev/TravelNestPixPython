# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#

import re
import sys
import os
from urllib.parse import unquote

sys.path.append(os.path.join(os.path.dirname(__file__), '/'))


from concurrent import futures
import logging

import grpc

from service.codeGeneration import genqrcode_pb2, genqrcode_pb2_grpc
from service.codeGeneration.PixCodeGenerator import PixCodeGenerator
import db.load
from efipay import EfiPay
import credentials
class Generator(genqrcode_pb2_grpc.GenQrCodeServiceServicer):
    def Generate(self, request, context):
        cmd = request.rq.split()
        gen = PixCodeGenerator()
        peer = context.peer()
        ip = ''
        match = re.match(r"ipv6:%5B([\w:.]+)%5D:\d+", peer)
        if match:
            ipv6_address = match.group(1)
            ip = unquote(ipv6_address)
        print(cmd)
        code = gen.generate_pix_code(cmd[0], cmd[1], cmd[2], cmd[3], ip, cmd[4], cmd[5], cmd[6], cmd[7], cmd[8])
        
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

# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
import psycopg2
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


db_user = 'postgres'
db_password = '12345'
db_host = 'localhost'
db_port = '5432'
db_name = 'travelnest_pix'

conn_str = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
conn = psycopg2.connect(dbname='postgres', user=db_user, password=db_password, host=db_host, port=db_port)
conn.autocommit = True

cur = conn.cursor()
cur.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{db_name}'")
exists = cur.fetchone()

if not exists:
    cur.execute(f'CREATE DATABASE {db_name}')
cur.close()
conn.close()

Base = declarative_base()

import sys
import os

import psycopg2

sys.path.append(os.path.join(os.path.dirname(__file__), 'service/qrCodeGeneration/'))



from concurrent import futures
import logging

import grpc

from service.qrCodeGeneration import genqrcode_pb2, genqrcode_pb2_grpc

class Generator(genqrcode_pb2_grpc.GenQrCodeServiceServicer):
    def Generate(self, request, context):
        for item in request:
            print(item)
        return genqrcode_pb2.responseCode(res="Cob %s" % request.rq)


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

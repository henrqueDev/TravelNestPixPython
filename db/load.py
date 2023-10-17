
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '/'))

from dotenv import load_dotenv
import psycopg2
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from db.base import Base

load_dotenv()

conn_str = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

conn = psycopg2.connect(dbname="postgres", user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))
        


conn.autocommit = True
cur = conn.cursor()
cur.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{os.getenv('DB_NAME')}' ")
exists = cur.fetchone()

if not exists:
    cur.execute(f"CREATE DATABASE {os.getenv('DB_NAME')}")

cur.close()
conn.close()

engine = create_engine(conn_str)
Base.metadata.create_all(engine)
print("rodou criacao tabelas")
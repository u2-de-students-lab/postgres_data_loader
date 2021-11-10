import argparse
import os

from dotenv import load_dotenv
import psycopg2

load_dotenv()

db = os.getenv('DATABASE')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
user = os.getenv('USER')
port = os.getenv('PORT')

parser = argparse.ArgumentParser(description='Paste path to file')

parser.add_argument('path', type=str, help='Put path to ur csv file')

path = parser.parse_args()

conn = psycopg2.connect(database=db, user=user, password=password, host=host, port=port)
  
cursor = conn.cursor()

with open(path.path) as fl:
    next(fl)
    cursor.copy_expert("COPY train FROM STDIN WITH CSV", fl)

conn.commit()
conn.close()





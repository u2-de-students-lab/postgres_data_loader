import argparse
import os
from argparse import Namespace

import psycopg2
from dotenv import load_dotenv


def cli() -> Namespace:

    parser = argparse.ArgumentParser()
    parser.add_argument('user_csv', type=str, help='Put path to ur csv file')
    cli_arguments  = parser.parse_args()

    return cli_arguments 


def db_loader(path: str) -> None:

    db = os.environ.get('DATABASE')
    password = os.environ.get('PASSWORD')
    host = os.environ.get('HOST')
    user = os.environ.get('USER')
    port = os.environ.get('PORT')

    conn = psycopg2.connect(database=db, user=user, password=password, host=host, port=port)

    cursor = conn.cursor()

    with open(path) as fl:
        next(fl)
        cursor.copy_expert("COPY train FROM STDIN WITH CSV", fl)

    conn.commit()
    conn.close()


def main() -> None:

    arguments = cli()

    load_dotenv()
    
    db_loader(path=arguments.user_csv)


if __name__ == '__main__':
    main()
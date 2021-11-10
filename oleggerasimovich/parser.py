import argparse
import os

from dotenv import load_dotenv
import psycopg2


def cli(user_csv: str):

    parser = argparse.ArgumentParser()
    parser.add_argument('user_csv', type=str, help='Put path to ur csv file')
    cli_arguments  = parser.parse_args([user_csv])

    return cli_arguments 


def main():

    user_csv = input('Paste path to your CSV file you want to parse: ')

    path = cli(user_csv=user_csv)

    load_dotenv()

    db = os.environ.get('DATABASE')
    password = os.environ.get('PASSWORD')
    host = os.environ.get('HOST')
    user = os.environ.get('USER')
    port = os.environ.get('PORT')

    conn = psycopg2.connect(database=db, user=user, password=password, host=host, port=port)

    cursor = conn.cursor()

    with open(path.user_csv) as fl:
        next(fl)
        cursor.copy_expert("COPY train FROM STDIN WITH CSV", fl)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
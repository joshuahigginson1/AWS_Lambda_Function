""" A Lambda function to connect to an RDS Instance. """

import pymysql
from os import getenv

rds_host = getenv("RDS_ENDPOINT")
username = getenv("RDS_ROOT_USER")
password = getenv("RDS_ROOT_PASS")
db_name = getenv("RDS_DB_NAME")


def get_events():
    print(f"Getting users...")
    result = []
    connection = pymysql.connect(host=rds_host,
                                 user=username,
                                 password=password,
                                 db=db_name,
                                 connect_timeout=5)

    with connection.cursor() as cursor:

        cursor.execute("""select * from test""")

        for row in cursor:
            result.append(list(row))

            connection.commit()
            cursor.close()

    return result


def lambda_handler(event, context):
    return get_events()

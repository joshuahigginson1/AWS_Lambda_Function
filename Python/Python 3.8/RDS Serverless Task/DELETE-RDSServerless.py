""" A Lambda function to DELETE data in an RDS Instance. """

import pymysql
from os import getenv

rds_host = getenv("RDS_ENDPOINT")
username = getenv("RDS_ROOT_USER")
password = getenv("RDS_ROOT_PASS")
db_name = getenv("RDS_DB_NAME")


def update_events():
    print("Deleting the user...")

    connection = pymysql.connect(host=rds_host,
                                 user=username,
                                 password=password,
                                 db=db_name,
                                 connect_timeout=5)

    with connection.cursor() as cursor:

        cursor.execute("""DELETE FROM test WHERE id=%s """ % (event['id']))

        connection.commit()
        cursor.close()

    print(f"User {event['id']} deleted.")


def lambda_handler(event, context):
    return update_events()

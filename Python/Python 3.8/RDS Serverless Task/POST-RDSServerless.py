""" A Lambda function to connect to an RDS Instance. """

import pymysql
from os import getenv

rds_host = getenv("RDS_ENDPOINT")
username = getenv("RDS_ROOT_USER")
password = getenv("RDS_ROOT_PASS")
db_name = getenv("RDS_DB_NAME")


def save_events(event):
    print(f"Adding User {event['name']}...")
    result = []
    connection = pymysql.connect(host=rds_host,
                                 user=username,
                                 password=password,
                                 db=db_name,
                                 connect_timeout=5)

    with connection.cursor() as cursor:
        cursor.execute("""insert into test (id, name) values(%s, '%s')""" % (
        event['id'], event['name']))
        cursor.execute("""select * from test""")
        for row in cursor:
            result.append(list(row))

        connection.commit()
        cursor.close()

        print("Data from RDS...")
        print(result)


def lambda_handler(event, context):
    save_events(event)

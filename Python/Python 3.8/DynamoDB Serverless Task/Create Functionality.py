"""

An AWS Lambda Function to add CREATE functionality to our dynamoDB
database.

"""

from __future__ import print_function  # Python 2/3 compatibility
import boto3
import json
import decimal


def lambda_handler(event, context):
    # Helper class to convert a DynamoDB item to JSON.
    class DecimalEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, decimal.Decimal):
                if abs(o) % 1 > 0:
                    return float(o)
                else:
                    return int(o)
            return super(DecimalEncoder, self).default(o)

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')

    title = '{}'.format(event['title'])
    year = '{}'.format(event['year'])

    response = table.put_item(
        Item={
            'Title':title,
            'Year':year,
            'Rating':5
        }
    )

    print(table.creation_date_time)
    print("PutItem succeeded:")
    print(json.dumps(response, indent=4, cls=DecimalEncoder))

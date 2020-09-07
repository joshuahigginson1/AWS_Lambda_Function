""" An AWS Lambda Function to create an EC2 Instance."""

# Import Boto3.
import boto3


def lambda_handler(event, context):

    # Create EC2 Connection

    ec2 = boto3.resource('ec2')

    # Create a new ec2 instance.

    ec2.create_instances(
        ImageId='ami-04137ed1a354f54c4',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='asbandia-key-pair',
        Placement={'AvailabilityZone': 'eu-west-1a'}
    )


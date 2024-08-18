import os

import boto3

def init_db() -> None:
    dynamodb = boto3.resource(
        os.environ("DB_NAME"), region_name=os.environ("DB_REGION_NAME")
    )
    table = dynamodb.Table(os.environ("DB_TABLE_NAME"))
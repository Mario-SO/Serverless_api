import json
import os
import time
import uuid
import boto3

dynamo = boto3.client('dynamodb')
dynamoTable = dynamo.table(os.environ['dynamoTableName'])

def create(event, context):

    print (event)
    userId = event['User']
    Note = event['Note']

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
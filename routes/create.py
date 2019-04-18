import json
import os
import time
import uuid
import boto3

dynamo = boto3.resource('dynamodb')
dynamoTable = dynamo.Table(os.environ['dynamoTableName'])

def create(event, context):
    print(event)

    item={
        'userId': event['User'],
        'noteId': str(uuid.uuid4()),
        'noteContent': event['Note'],
        'date': int(time.time() * 1000)
    }

    headers = {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Credentials": "true"
    }

    response = dynamoTable.put_item(Item=item)

    response = {
        "headers": headers,
        "statusCode": 200,
        "body": json.dumps('Created Succesfully')
    }

    return response
import json
import os
import time
import uuid
import boto3
import simplejson as json

dynamo = boto3.resource('dynamodb')
dynamoTable = dynamo.Table(os.environ['dynamoTableName'])

def get(event, context):
    print(event)

    item={
        'userId': event['userId'],
        'noteId': event['noteId']
    }

    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "true"
    }

    dynamoResponse = dynamoTable.get_item(Key=item)
    #print(dynamoResponse)

    response = {
        "headers": headers,
        "statusCode": 200,
        "body": json.dumps(dynamoResponse['Item'])
    }

    return response
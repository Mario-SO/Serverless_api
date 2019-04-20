import datetime
import json, uuid
from libs.resourcesLibs import dynamoTable
from libs.responsesLibs import success, failure, unauthorized
from boto3.dynamodb.conditions import Attr


def update(event, context):
    print(event)
     
    # Load request body and pathParameters
    pathParameters = event['pathParameters']
    userId = event['requestContext']['identity']['cognitoIdentityId']

    try:
        body = json.loads(event['body'])
        item={
            'userId': userId,
            'id': pathParameters['id'],
            'noteContent': body['note'],
            'creationDate': str(datetime.datetime.now())
        }
        dynamoTable.put_item(
            Item=item, 
            ConditionExpression = Attr('id').exists() & Attr('userId').eq(userId)
        )
        return success({"status": True})
    except Exception as e:
        print(e)
        return failure({"status": False})

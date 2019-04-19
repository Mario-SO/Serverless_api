import datetime
import json, uuid
from libs.resourcesLibs import dynamoTable
from libs.responsesLibs import success, failure, unauthorized
from boto3.dynamodb.conditions import Attr


def update(event, context):
    print(event)

    # Check for cognitoIdentiyId
    try:
        userId = event['requestContext']['identity']['cognitoIdentityId']
    except:
        return unauthorized()
      
    # Load request body and pathParameters
    body = json.loads(event['body'])
    pathParameters = event['pathParameters']

    try:
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

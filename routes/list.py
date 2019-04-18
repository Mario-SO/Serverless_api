from libs.resourcesLibs import dynamoTable
from libs.responsesLibs import success, failure
from boto3.dynamodb.conditions import Attr
import json

def list(event, context):
    print(event)

    body = json.loads(event['body'])

    try:
        dynamoResponse = dynamoTable.scan(FilterExpression=Attr('userId').eq(body['userId']))
        response = success(dynamoResponse['Items']) 
        
        if dynamoResponse['Items'] == []:
            raise Exception

    except Exception as e:
        print(e)
        response = failure('That user doesn\'t exist')

    return response
from libs.resourcesLibs import dynamoTable
from libs.responsesLibs import success, failure, unauthorized
from boto3.dynamodb.conditions import Attr
import json

def list(event, context):
    print(event)

    # Query dynamoDB
    try:
        dynamoResponse = dynamoTable.scan(
            FilterExpression=Attr('userId').eq(event['requestContext']['identity']['cognitoIdentityId'])
        )
        if dynamoResponse['Items'] == []:
            return failure({"status": False, "error": "No items found"})
        else:
            return success(dynamoResponse['Items']) 
    except Exception as e:
        print(e)
        response = failure({"status": False})
    return response
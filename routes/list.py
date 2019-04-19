from libs.resourcesLibs import dynamoTable
from libs.responsesLibs import success, failure, unauthorized
from boto3.dynamodb.conditions import Attr
import json

def list(event, context):
    print(event)

    # Check for cognitoIdentiyId
    try:
        userId = event['requestContext']['identity']['cognitoIdentityId']
    except:
        return unauthorized()

    # Query dynamoDB
    try:
        dynamoResponse = dynamoTable.scan(FilterExpression=Attr('userId').eq(userId))
        if dynamoResponse['Items'] == []:
            return failure({"status": False, "error": "No items found"})
        else:
            return success(dynamoResponse['Items']) 
    except Exception as e:
        print(e)
        response = failure({"status": False})
    return response
from libs.resourcesLibs import dynamoTable
from libs.responsesLibs import success, failure, unauthorized
import json

def delete(event, context):
    print(event)
     
    # Load pathParameters, if no parameters, it wil load null, could integrate error handling
    pathParameters = event['pathParameters']

    # Write to dynamoDB -> delete item
    try:
        item={
            'userId': event['requestContext']['identity']['cognitoIdentityId'],
            'id': pathParameters['id']
        }
        response = dynamoTable.delete_item(Key=item, ReturnValues='ALL_OLD')
        try:
            response['Attributes']
            return success({"status": True})
        except:
            return failure({"status": False, "error": "item not found."})
    except Exception as e:
        print(e)
        return failure({"status": False})

from libs.resourcesLibs import dynamoTable
from libs.responsesLibs import success, failure, unauthorized
import json

def get(event, context):
    print(event)

    # Load pathParameters, if no parameters, it wil load null, could integrate error handling
    pathParameters = event['pathParameters']

    try:
        item={
            'userId': event['requestContext']['identity']['cognitoIdentityId'],
            'id': pathParameters['id']
        }
        dynamoResponse = dynamoTable.get_item(Key=item)
        try:
            return success(dynamoResponse['Item'])
        except:
            return failure({"status": False, "error": "Item not found." })
    except Exception as e:
        print(e)
        return failure({"status": False})

from libs.resourcesLibs import dynamoTable
from libs.responsesLibs import success, failure, unauthorized
import json

def get(event, context):
    print(event)

    # Check for cognitoIdentiyId
    try:
        userId = event['requestContext']['identity']['cognitoIdentityId']
    except:
        return unauthorized()

    pathParameters = event['pathParameters']

    try:
        item={
            'userId': userId,
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

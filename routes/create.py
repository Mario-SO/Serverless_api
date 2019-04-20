import datetime
import uuid
import json
from libs.resourcesLibs import dynamoTable
from libs.responsesLibs import success, failure, unauthorized

def create(event, context):
    print(event)
    
    try:
        # Load request body
        body = json.loads(event['body'])

        # Write to dynamoDB -> create item
        item={
            'userId': event['requestContext']['identity']['cognitoIdentityId'],
            'id': str(uuid.uuid4()),
            'noteContent': body['note'],
            'creationDate': str(datetime.datetime.now())
        }
        dynamoTable.put_item(Item=item)
        return success(item)
    except Exception as e:
        print(e)
        return failure({"status": False})

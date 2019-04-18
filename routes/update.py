import datetime
import json
from libs.resourcesLibs import dynamoTable
from libs.responsesLibs import success, failure

def update(event, context):
    print(event)

    body = json.loads(event['body'])

    item={
        'userId': body['userId'],
        'noteId': body['noteId']
    }

    try:
        dynamoTable.update_item(Key=item, UpdateExpression='SET noteContent = :val1, creationDate = :val2',
        ExpressionAttributeValues={
        ':val1': body['note'],
        ':val2': str(datetime.datetime.now()) 
            }
        )
        response = success('Updated Succesfully')
    except Exception as e:
        print(e)
        response = failure('Could not update item')

    return response
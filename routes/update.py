import datetime
from libs.resourcesLibs import dynamoTable
from libs.responsesLibs import success, failure

def update(event, context):
    print(event)

    item={
        'userId': event['userId'],
        'noteId': event['noteId'],
    }

    try:
        dynamoTable.update_item(Key=item, UpdateExpression='SET noteContent = :val1',
        ExpressionAttributeValues={
        ':val1': event['note']
            }
        )
        response = success('Updated Succesfully')
    except Exception as e:
        print(e)
        response = failure('Could not update item')

    return response
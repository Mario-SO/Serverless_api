from libs.resourcesLibs import dynamoTable
from libs.responsesLibs import success, failure
import json

def delete(event, context):
    print(event)

    body = json.loads(event['body'])

    item={
        'userId': body['userId'],
        'noteId': body['noteId']
    }

    try:
      dynamoTable.delete_item(Key=item)
      response = success('Item deleted successfully')
    except Exception as e:
      print(e)
      response = failure('That Item couldn\'t be deleted')

    return response
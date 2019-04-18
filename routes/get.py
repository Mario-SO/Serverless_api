from libs.resourcesLibs import dynamoTable
from libs.responsesLibs import success, failure
import json

def get(event, context):
    print(event)

    body = json.loads(event['body'])

    item={
        'userId': body['userId'],
        'noteId': body['noteId']
    }

    try:
      dynamoResponse = dynamoTable.get_item(Key=item)
      response = success(dynamoResponse['Item'])
    except Exception as e:
      print(e)
      response = failure('That Item doesn\'t exist')

    return response
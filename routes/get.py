import time
import uuid
import simplejson as json
from libs.resourcesLibs import dynamoTable
from libs.responsesLibs import success, failure

def get(event, context):
    print(event)

    item={
        'userId': event['userId'],
        'noteId': event['noteId']
    }

    dynamoResponse = dynamoTable.get_item(Key=item)
    #print(dynamoResponse)

    try:
      dynamoTable.get_item(Item=item)
      response = success(json.dumps(dynamoResponse['Item']))
    except Exception as e:
      print(e)
      response = failure('That Item doesn\'t exist')

    return response
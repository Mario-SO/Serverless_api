import json
import time
import uuid
from libs.resourcesLibs import dynamoTable
from libs.responsesLibs import success, failure

def create(event, context):
    print(event)

    item={
        'userId': event['User'],
        'noteId': str(uuid.uuid4()),
        'noteContent': event['Note'],
        'date': int(time.time() * 1000)
    }

    try:
      dynamoTable.put_item(Item=item, Exists=True)
      response = success('Created Succesfully')
    except Exception as e:
      print(e)
      response = failure('Could not create item')

    return response
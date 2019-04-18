import datetime
import uuid
from libs.resourcesLibs import dynamoTable
from libs.responsesLibs import success, failure

def create(event, context):
    print(event)

    item={
        'userId': event['userId'],
        'noteId': str(uuid.uuid4()),
        'noteContent': event['note'],
        'date': str(datetime.datetime.now())
    }

    try:
      dynamoTable.put_item(Item=item)
      response = success('Created Succesfully')
    except Exception as e:
      print(e)
      response = failure('Could not create item')

    return response
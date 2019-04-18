from libs.resourcesLibs import dynamoTable
from libs.responsesLibs import success, failure

def get(event, context):
    print(event)

    item={
        'userId': event['userId'],
        'noteId': event['noteId']
    }

    try:
      dynamoResponse = dynamoTable.get_item(Key=item)
      response = success(dynamoResponse['Item'])
    except Exception as e:
      print(e)
      response = failure('That Item doesn\'t exist')

    return response
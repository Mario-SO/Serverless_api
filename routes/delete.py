from libs.resourcesLibs import dynamoTable
from libs.responsesLibs import success, failure

def delete(event, context):
    print(event)

    item={
        'userId': event['userId'],
        'noteId': event['noteId']
    }

    try:
      dynamoTable.delete_item(Key=item)
      response = success('Item deleted successfully')
    except Exception as e:
      print(e)
      response = failure('That Item couldn\'t be deleted')

    return response
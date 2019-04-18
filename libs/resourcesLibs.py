import boto3
import os

dynamo = boto3.resource('dynamodb')
dynamoTable = dynamo.Table(os.environ['dynamoTableName'])
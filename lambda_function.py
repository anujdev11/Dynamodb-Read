import json,ast
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from datetime import datetime


def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    tableName = "receiveData1"
    table = dynamodb.Table(tableName)
    response = table.get_item(
        Key={
            'Raspberry_Id':'0000000068480410',
        }
    )
    item1 = response['Item']
    item=ast.literal_eval(json.dumps(item1))
    print(item)
    RaspberryId=item['Raspberry_Id']
    ReceivedData=item['Received_Data']
    
    print(type(RaspberryId))
    return({
    "isBase64Encoded": True,
    "statusCode": 200,
    "headers": { 'Access-Control-Allow-Origin': '*'},
    "body": {
            "Raspberry_Id": RaspberryId,
            "Received_Data": ReceivedData
        }
    })
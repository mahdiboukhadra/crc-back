import json
import boto3
    
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('visitcount')

    response = table.get_item(
        Key={
            'id':'1'
        })
    
    views = response['Item']['views']

    views = views + 1
    
    table.put_item(
   Item={
        'id': '1',
        'views':views
    }
)
    return views
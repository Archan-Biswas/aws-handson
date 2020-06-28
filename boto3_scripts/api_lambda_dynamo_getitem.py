import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user')

def lambda_handler(event, context):
    userid = event['userid']
    response = table.get_item(
    Key={
        'userid': userid
    }
    )
    return response['Item']
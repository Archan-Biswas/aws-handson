import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user')

def lambda_handler(event, context):
    response = table.put_item(Item=event)
    return{
        "code":200,
        "message":"item loaded successfully"
}
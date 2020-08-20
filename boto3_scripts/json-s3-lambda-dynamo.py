import json
import boto3

s3_con_cli = boto3.client(service_name='s3',region_name='ap-south-1')
dynamo_rsc = boto3.resource(service_name='dynamodb',region_name='ap-south-1')

# load json data in S3 bucket and triggers lambda function -----
# lambda function loads the data to dynamo db table -----------
def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    obj_name = event['Records'][0]['s3']['object']['key']
    json_obj = s3_con_cli.get_object(Bucket=bucket_name,Key=obj_name)
    jsonFileReader = json_obj['Body'].read()
    json_dict = json.loads(jsonFileReader)
    table = dynamo_rsc.Table('employees')
    print(json_dict)
    for each in json_dict:
        table.put_item(Item=each)
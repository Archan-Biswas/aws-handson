import boto3

s3_con_cli = boto3.client(service_name='s3',region_name='ap-south-1')
dynamo_rsc = boto3.resource(service_name='dynamodb',region_name='ap-south-1')
table = dynamo_rsc.Table('customers')

# load csv data in S3 bucket and triggers lambda function -----
# lambda function loads the data to dynamo db table -----------
def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    obj_name = event['Records'][0]['s3']['object']['key']
    csv_obj = s3_con_cli.get_object(Bucket=bucket_name,Key=obj_name)
    data = csv_obj['Body'].read().decode("utf-8")
    customer = data.split("\n")
    for cst in customer:
        cst_data = cst.split(",")
        try:
            table.put_item(
            Item = {
                "Custid" : cst_data[0],
                "Custname" : cst_data[1],
                "Location" : cst_data[2]
            }
            )
        except Exception as e:
            print("EOF")
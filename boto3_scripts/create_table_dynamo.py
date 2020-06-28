import boto3

aws_mng_con=boto3.session.Session(profile_name="user01")
dynamo_con_re=aws_mng_con.resource('dynamodb','ap-south-1')

## CREATE A DYNAMO DB TABLE
dynamo_con_re.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'empid',
            'AttributeType': 'S'
        }
    ],
    TableName='employee',
    KeySchema=[
        {
            'AttributeName': 'empid',
            'KeyType': 'HASH'
        }
    ],
    BillingMode='PROVISIONED',
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
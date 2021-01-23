import boto3
import json 

s3_client = boto3.client("s3")

def lambda_handler(event, context):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]

    filename = event["Records"][0]["s3"]["object"]["key"]

    json_object = boto3.client("s3").get_object(
        bucket = bucket, 
        key = filename 
    )

    dynamodb = boto3.resource('dynamodb')

    json_parse = json_object["Body"].read()
    json_diction = json.loads(json_parse)

    dynamo_table = dynamodb.Table("Employees")
    dynamo_table.put_item(item = json_diction)


    #print("Heres the right bucket + object: {0} {1}").format(bucket, filename)    #this is for s3 verification
    return "hey from lambda"
    

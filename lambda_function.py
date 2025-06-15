import json
import boto3
import csv
import urllib.parse

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get bucket and object key from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        lines = response['Body'].read().decode('utf-8').splitlines()
        reader = csv.DictReader(lines)

        for row in reader:
            print(f"Processing record: {row}")
            # You can add code to write to DynamoDB or further process each row

        return {
            'statusCode': 200,
            'body': json.dumps('File processed successfully!')
        }

    except Exception as e:
        print(e)
        raise e

import json
import boto3


def like(email, article_id):
    region_name = 'us-east-1'
    dynamodb = boto3.resource('dynamodb', region_name=region_name)
    table = dynamodb.Table('ifashion-likes')
    response = table.get_item(
        Key={
            'email': email
        }
    )
    if 'Item' in response:
        likes_list = response['Item']['likes']
        if article_id not in likes_list:
            likes_list.append(article_id)
            response = table.update_item(
                Key={
                    'email': email
                },
                UpdateExpression="set likes=:l",
                ExpressionAttributeValues={':l': likes_list},
                ReturnValues="UPDATED_NEW"
            )
            print(response)
    else:
        liked_list = []
        liked_list.append(article_id)
        response = table.put_item(
                Item={
                    "email": email,
                    "likes": liked_list
                },
            )
        print(response)
        

def lambda_handler(event, context):
    username = event['queryStringParameters']['username']
    article_id = event['queryStringParameters']['id']
    # TODO implement
    like(username, article_id)
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps('Hello from Lambda!')
    }

import json
import boto3
import uuid

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = dynamodb.Table('MessagesTable')
    
    # Handle POST request
    if event['httpMethod'] == 'POST':
        data = json.loads(event['body'])
        messageId = str(uuid.uuid4())
        table.put_item(Item={'messageId': messageId, 'message': data['message']})
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'  # Important for CORS
            },
            'body': json.dumps({'messageId': messageId, 'message': data['message']})
        }
    
    # Handle GET request
    elif event['httpMethod'] == 'GET':
        result = table.scan()
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'  # Important for CORS
            },
            'body': json.dumps(result['Items'])
        }
cd prod
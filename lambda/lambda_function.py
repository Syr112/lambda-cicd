import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello Updated from Lambda VScode')
    }# final trigger test

# force trigger after fresh deploy reset
import json

def buildResponse(statusCode, body):
    response = {
        "statusCode": statusCode,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true"
        },
        "body": json.dumps(body)
    }
    return response

def success(body):
    return buildResponse(200, body)

def failure(body):
    return buildResponse(500, body)

def unauthorized():
    return buildResponse(401, "Access denied")
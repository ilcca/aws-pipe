import json
import joblib

# In AWS, you would download model from S3 or package it
model = joblib.load('/tmp/model.pkl')  # placeholder

def lambda_handler(event, context):
    input_data = event["input"]
    prediction = model.predict([input_data]).tolist()
    return {
        "statusCode": 200,
        "body": json.dumps({"prediction": prediction})
    }
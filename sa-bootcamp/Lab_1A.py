import json
import os
import sys
import logging
import boto3
import botocore
import datetime
import time

from anthropic import AnthropicBedrock
from botocore.exceptions import ClientError

class ImageError(Exception):
    "Custom exception for errors returned by Amazon &titan-text-express; model"
    def __init__(self, message):
        self.message = message
        
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

bedrock = boto3.client(service_name='bedrock-runtime')
cloudwatch = boto3.client('cloudwatch')

def invoke_claude_v3_sonnet(question):
    
    try:
        # Specify the input data and model ID
        input_data = "{\"messages\":[{\"role\":\"user\",\"content\":[{\"type\":\"text\",\"text\":\"Write python code for uploading the image to Amazon S3 bucket\\nCertainly! Here's an example of python code to upload an image to Amazon S3 bucket:\\n\\n....\"}]}],\"anthropic_version\":\"bedrock-2023-05-31\",\"max_tokens\":2000}"
        
        model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'
        # Invoke the model for inference
        current_time1 = time.time() # first moment
        response = bedrock.invoke_model(contentType='application/json', body=input_data, modelId=model_id)
        current_time2 = time.time() # second moment
        
        time_span = current_time2 - current_time1
        
        # Retrieve the inference response
        inference_result = response['body'].read().decode('utf-8')
        print("Text_V3_sonnet:"+ str(current_time1) + ";" + str(time_span))
        put_execution_data("Claude-v3-sonnet", time_span) 
        # Process the inference result
        print(inference_result)
        response_body = json.loads(inference_result)
        return inference_result   
    
    except ClientError:
        logger.error("Couldn't invoke Claud-V3-sonnet")
        raise
    
def invoke_claude_v3_haiku(question):
    
    try:
        # Specify the input data and model ID
        input_data = "{\"messages\":[{\"role\":\"user\",\"content\":[{\"type\":\"text\",\"text\":\"Write python code for uploading the image to Amazon S3 bucket\\nCertainly! Here's an example of python code to upload an image to Amazon S3 bucket:\\n\\n....\"}]}],\"anthropic_version\":\"bedrock-2023-05-31\",\"max_tokens\":2000}"
        
        model_id = 'anthropic.claude-3-haiku-20240307-v1:0'
        # Invoke the model for inference
        current_time1 = time.time() # first moment
        response = bedrock.invoke_model(contentType='application/json', body=input_data, modelId=model_id)
        current_time2 = time.time() # second moment
        
        time_span = current_time2 - current_time1
        
        # Retrieve the inference response
        inference_result = response['body'].read().decode('utf-8')
        print("Text_V3_Haiku:"+ str(current_time1) + ";" + str(time_span))
        put_execution_data("Claude-v3-haiku", time_span) 
        # Process the inference result
        print(inference_result)
        response_body = json.loads(inference_result)
        return inference_result   
    
    except ClientError:
        logger.error("Couldn't invoke Claud-V3-haiku")
        raise
    
def put_execution_data(dimension, value):
    cloudwatch = boto3.client('cloudwatch')

    # Put custom metrics
    cloudwatch.put_metric_data(
    MetricData=[
        {
            'MetricName': 'execution_time',
            'Dimensions': [
                {
                    'Name': 'llm',
                    'Value': dimension
                },
            ],
            'Unit': 'Seconds',
            'Value': value
        },
    ],
    Namespace='bedrock/llm_metrics'
    )
    print("Dimension: "+ dimension + " | Value: " + str(value))
    return "OK"

def main():
    
    invoke_claude_v3_sonnet("Teste")
    invoke_claude_v3_haiku("Teste")
    
main()
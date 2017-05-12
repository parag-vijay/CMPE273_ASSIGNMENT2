# -*- coding: utf-8 -*-
import boto3

def handler(event, context):
    # Your code goes here!
    try:
        table = boto3.resource("dynamodb").Table("order")
        order_id = {"order_id":event["order_id"]}
        result = table.get_item(Key = order_id)
        return result["Item"]
    except Exception as e:
        return e.message
    

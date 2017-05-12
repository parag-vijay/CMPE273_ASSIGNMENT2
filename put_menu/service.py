# -*- coding: utf-8 -*-
import boto3

def handler(event, context):
    # Your code goes here!
    try:
        table = boto3.resource("dynamodb").Table("menu")
        menu_id = {"menu_id": event["menu_id"]}
        keyName = event["body"].keys()[0]
        values = event["body"][keyName]
        table.update_item(Key=menu_id, UpdateExpression="SET #key = :val",ExpressionAttributeNames={"#key":keyName}, ExpressionAttributeValues={ ":val" :values})
        return "200 OK"
    except Exception as e:
        return e.message
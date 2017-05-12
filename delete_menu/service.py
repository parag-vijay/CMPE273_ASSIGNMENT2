# -*- coding: utf-8 -*-
import boto3

def handler(event, context):
    # Your code goes here!
    try:
        table = boto3.resource("dynamodb").Table('menu')
        menu_id = {"menu_id":event["menu_id"]}
        table.delete_item(Key = menu_id)
    except Exception as e:
        return e.message
    return "200 OK"
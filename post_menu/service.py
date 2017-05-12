# -*- coding: utf-8 -*-
import json

import boto3


def handler(event, context):
    # Your code goes here!
    try:
        table = boto3.resource('dynamodb').Table('menu')
        menu = event["menuBody"]
        result = table.put_item(Item = menu)
    except Exception as e:
        return e.message
    return "200 OK"
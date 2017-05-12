# -*- coding: utf-8 -*-
import boto3

def handler(event, context):
    # Your code goes here!
    try:
        order_table = boto3.resource("dynamodb").Table("order")
        order_body = event["body"]
        order_table.put_item(Item = order_body, ReturnValues = "ALL_OLD")

        query = "Hi "
        query = query + order_body["customer_name"]
        query = query + " please choose one of the following selection: "

        menu_table = boto3.resource("dynamodb").Table("menu")
        menu_id = {"menu_id":order_body["menu_id"]}
        menu_result = menu_table.get_item(Key = menu_id)
        selection_list = menu_result["Item"]["selection"]
        for i in range(len(selection_list)) :
            query = query + " "+str(i+1) + ". " + selection_list[i]
        
        return {"Message":query}
    except Exception as e:
        return e.message
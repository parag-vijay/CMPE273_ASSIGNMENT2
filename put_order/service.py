# -*- coding: utf-8 -*-
import boto3
import datetime

def handler(event, context):
    # Your code goes here!
    try:
        order_id = {"order_id": event["order_id"]}
        order_table = boto3.resource("dynamodb").Table("order")
        order_result = order_table.get_item(Key = order_id)

        choice = int(event["input"])
        menu_table = boto3.resource("dynamodb").Table("menu")
        menu_id = {"menu_id" : order_result["Item"]["menu_id"]}
        menu_result = menu_table.get_item(Key = menu_id)

        if "order" not in order_result["Item"]:
            order_body =  {"selection" : menu_result["Item"]["selection"][choice-1]}
            order_table.update_item(Key = order_id, UpdateExpression = "SET #key = :value1", ExpressionAttributeNames = {"#key":"order"}, ExpressionAttributeValues = {":value1":order_body})
            query = "Which size do you want ?"
            size_list = menu_result["Item"]["size"]
            for i in range(len(size_list)):
                query = query + " " + str(i+1) + ". " + size_list[i]
            return {"message": query}
        else:
            now = datetime.datetime.now()
            order_body = {"selection" : order_result["Item"]["order"]["selection"]}
            order_body["size"] = menu_result["Item"]["size"][choice-1]
            order_body["costs"] = menu_result["Item"]["price"][choice-1]
            order_body["order_time"] =  now.strftime("%m-%d-%Y@%H:%M:%S")
            order_table.update_item(Key = order_id, UpdateExpression = "SET order_status = :value1, #key = :value2",ExpressionAttributeNames = {"#key":"order"}, ExpressionAttributeValues = {":value1":"Processing", ":value2":order_body})
            return {"message" : "Your order costs $%s. We will email you when the order is ready. Thank you!"% order_body["costs"]}
    except Exception as e:
        return e.message